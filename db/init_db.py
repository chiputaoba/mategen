# -*- coding: utf-8 -*-
"""
Author: MuYu_Cheney
"""

from sqlalchemy import create_engine, text
from config.config import username, password, hostname, database_name
from db.base import Base, engine, SessionLocal
from db.base_model import SecretModel, ThreadModel, KnowledgeBase, FileInfo, DbBase, MessageModel


# 检查数据库是否存在，并在需要时创建数据库
def create_database_if_not_exists(username: str, password: str, hostname: str, database_name: str):
    # 创建一个连接到数据库的引擎（没有指定数据库名）
    engine_for_check = create_engine(f"mysql+pymysql://{username}:{password}@{hostname}?charset=utf8mb4")

    with engine_for_check.connect() as connection:
        # 执行 SQL 查询，检查数据库是否存在
        result = connection.execute(text(f"SHOW DATABASES LIKE '{database_name}'"))
        if result.fetchone() is None:
            # 数据库不存在，执行创建数据库
            connection.execute(
                text(f"CREATE DATABASE {database_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
            print(f"Database '{database_name}' created successfully.")
        else:
            print(f"Database '{database_name}' already exists.")


# 定义数据库模型初始化函数
def initialize_database():
    try:
        # 检查数据库是否存在，如果不存在，先继续进行创建
        create_database_if_not_exists(username, password, hostname, database_name)

        # 创建所有表
        Base.metadata.create_all(engine)

    except Exception as e:
        print("Error occurred during database initialization:", e)
        return False


def delete_database():
    # 删除所有表
    Base.metadata.drop_all(engine)
    return True


if __name__ == '__main__':
    initialize_database()
    # delete_database()