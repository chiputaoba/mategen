from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import HTTPException, Body
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import logging
from db.base_model import DbBase

"""
官方文档：https://docs.sqlalchemy.org/en/20/dialects/mysql.html
"""

# 用于创建一个基类，该基类将为后续定义的所有模型类提供 SQLAlchemy ORM 功能的基础。
Base = declarative_base()


class DBConfig(BaseModel):
    hostname: str
    port: str
    username: str
    password: str
    database_name: str


def get_engine(db_config: DBConfig):
    uri = f"mysql+pymysql://{db_config.username}:{db_config.password}@{db_config.hostname}:{db_config.port}/{db_config.database_name}?charset=utf8mb4"
    engine = create_engine(uri, echo=True)
    return engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False)


def test_database_connection(db_config: DBConfig):
    """
    创建数据库连接，如果连接成功，返回该连接下所有数据库名称及对应的表名（不包含系统预设的数据库）
    :param db_config:
    :return:
    """

    uri = f"mysql+pymysql://{db_config.username}:{db_config.password}@{db_config.hostname}:{db_config.port}/{db_config.database_name}?charset=utf8mb4"
    engine = create_engine(uri, echo=True)

    SessionLocal.configure(bind=engine)
    session = SessionLocal()

    try:
        with engine.connect() as conn:
            conn.execute(text(f"USE `{db_config.database_name}`;"))
            tables = conn.execute(text("SHOW TABLES;"))
            table_list = [table[0] for table in tables]
        session.close()
        return table_list  # 直接返回表列表
    except SQLAlchemyError as e:
        session.close()
        raise HTTPException(status_code=400, detail=f"数据库连接失败: {str(e)}")
    except Exception as e:
        session.close()
        raise HTTPException(status_code=500, detail=f"内部服务器错误: {str(e)}")



def insert_db_config(db_config: DBConfig):
    """
    向数据库中插入一条新的数据库连接配置记录，并返回生成的 UUID。
    :param session: SQLAlchemy Session 对象，用于数据库操作
    :param hostname: 数据库服务器的主机名
    :param port: 数据库服务器的端口
    :param username: 用于连接数据库的用户名
    :param password: 用于连接数据库的密码
    :param database_name: 要连接的数据库名
    :return: 成功插入后的配置UUID，或在出现错误时返回 None
    """
    from config.config import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    SessionLocal.configure(bind=engine)
    session = SessionLocal()

    try:
        # 测试数据库连接
        test_database_connection(db_config)  # 如果连接失败，将抛出异常

        # 检查数据库中是否已经存在相同的配置
        existing_config = session.query(DbBase).filter(
            DbBase.hostname == db_config.hostname,
            DbBase.port == db_config.port,
            DbBase.username == db_config.username,
            DbBase.password == db_config.password,
            DbBase.database_name == db_config.database_name
        ).first()

        if existing_config:
            # 如果找到了现有配置，不执行插入操作
            session.close()
            raise HTTPException(status_code=400, detail="已存在相同的数据库配置，插入被拒绝")

        new_db_config = DbBase(
            hostname=db_config.hostname,
            port=db_config.port,
            username=db_config.username,
            password=db_config.password,
            database_name=db_config.database_name
        )
        session.add(new_db_config)
        session.commit()
        return str(new_db_config.id)  # 返回 UUID 字符串
    except HTTPException as http_ex:
        session.rollback()
        session.close()
        raise http_ex  # 重新抛出捕获的 HTTPException
    except Exception as e:
        session.rollback()
        session.close()
    raise HTTPException(status_code=500, detail=f"数据插入失败: {str(e)}")


def update_db_config(db_info_id: str, new_config: DBConfig):
    from config.config import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

    SessionLocal.configure(bind=engine)
    session = SessionLocal()

    try:
        # 测试新的数据库连接
        test_database_connection(new_config)  # 如果连接失败，将抛出异常

        # 查找现有的配置记录
        db_config = session.query(DbBase).filter(DbBase.id == db_info_id).first()
        if db_config:
            # 更新配置
            db_config.hostname = new_config.hostname
            db_config.port = new_config.port
            db_config.username = new_config.username
            db_config.password = new_config.password
            db_config.database_name = new_config.database_name

            session.commit()  # 提交更改
            return True
        else:
            return False
    except HTTPException as http_ex:
        session.rollback()
        raise http_ex  # 重新抛出 HTTPException，由上层处理
    except Exception as e:
        session.rollback()  # 回滚在异常情况下的所有更改
        raise HTTPException(status_code=500, detail=f"数据库操作失败: {str(e)}")
    finally:
        session.close()


def get_all_databases():
    from config.config import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

    SessionLocal.configure(bind=engine)
    session = SessionLocal()
    try:
        # 查询所有数据库配置，并只选取 id 和 database_name
        db_configs = session.query(DbBase.id, DbBase.database_name).order_by(DbBase.created_at.desc()).all()
        # 将查询结果格式化为列表字典
        result = [{"id": config.id, "database_name": config.database_name} for config in db_configs]
        session.close()
        return result
    except Exception as e:
        session.close()
        raise Exception(f"Failed to retrieve database configurations: {str(e)}")

def delete_db_config(db_info_id: str):
    from config.config import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

    SessionLocal.configure(bind=engine)
    session = SessionLocal()
    try:
        # 查找要删除的数据库配置对象
        db_config = session.query(DbBase).filter(DbBase.id == db_info_id).first()
        if db_config is None:
            session.close()
            return False  # 如果找不到对象，返回 False 表示无法删除

        # 删除找到的对象并提交更改
        session.delete(db_config)
        session.commit()
        return True  # 返回 True 表示删除成功
    except Exception as e:
        session.rollback()  # 发生错误时回滚
        raise Exception(f"Failed to delete database configuration: {str(e)}")
    finally:
        session.close()


def get_db_config_by_id(db_info_id: str):
    """
    从数据库中根据 ID 获取配置信息，并转换为 DBConfig 模型返回。
    """

    from config.config import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

    SessionLocal.configure(bind=engine)
    session = SessionLocal()

    db_info = session.query(DbBase).filter(DbBase.id == db_info_id).first()

    if db_info:
        return {key: value for key, value in db_info.__dict__.items() if not key.startswith('_')}
    else:
        return None
