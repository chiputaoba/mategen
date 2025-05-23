### 项目介绍

​		MateGen是一个交互式智能编程助手（Interactive Intelligent Programming Assistant），辅助用户高效完成智能数据分析、机器学习、深度学习和大模型开发等工作，并可根据用户实际需求定制知识库和拓展功能。

MateGen基础功能如下：

- **高易用性，零门槛调用**：MateGen为用户提供在线大模型应用服务，**无需任何硬件或网络代理门槛**，即可一键安装并开启对话；
- **强悍的高精度RAG系统**：一键同步本地文档并进行RAG检索问答，**最多支持1000篇文档以及10G文档内容进行检索**，支持md、ppt、word、pdf等主流文档格式高精度问答，能够高效率实现包括海量文档总结、大海捞针内容测试、情感倾向测试问答等功能。MateGen可根据用户问题自动识别是否需要进行RAG检索；
- **本地Python代码解释器**：可连接用户本地Python环境完成编程任务，包括数据清洗、数据可视化、机器学习、深度学习、大模型开发等代码工作编写，支持先学习代码库再进行编程、能够根据实际情况debug，支持可视化图片自动上传图床等功能；
- **高精度NL2SQL功能**：可根据用户需求编写SQL，并连接本地MySQL环境自动执行，可自动debug，并且支持先检索数据字典、企业数据知识库再进行SQL编写，从而提高SQL编写精度；
- 视觉能力和联网能力**：对话时输入图片网址即可开启MateGen视觉能力对图片内容进行识别，同时MateGen也具备联网能力，当遇到无法回答的问题时，可自动开启搜索问答模式；
- **无限对话上下文**：MateGen拥有无限上下文对话长度，MateGen会根据历史对话的未知信息密度进行合理处理，从而在节省token的同时实现无限对话上线文。
- MateGen具备**高稳定性**与**高可用性**，同时支持**Multi Function calling**（一个任务开启多个功能）和**Parallel Function calling**（一个功能开多个执行器），能够**自动分解复杂任务**、**自动Debug**，并且拥有一定程度“**自主意识**”，能够**审查自身行为**并深度**挖掘用户意图**。

### 启动项目

###### 1. 源码启动

1. 安装项目依赖

   ```bash
   pip install requirements.txt
   ```

2. 使用MySQL连接数据库

3. 在`metegen`->`config`->`config.py`中修改MySQL连接信息

4. 运行`metagen`->`api_server`->`api_router.py`以启动项目

5. 通过地址`http://ip:port`进行访问

### 项目架构

​	MateGen采用了目前最先进的threads-runs架构，以更好的进行用户历史消息对话管理以及自动修复运行中遇到的各种问题，同时采用了client与server分离架构，以确保最大程度Agent运行稳定性，同时支持多种不同类型底层大模型，MateGen基本结构如下：

<div align="center">
<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20240715001340035.png" alt="image-20240713010710534" width="600"/>
</div>