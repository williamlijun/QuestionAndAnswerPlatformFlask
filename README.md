## 项目结构


    question_and_answer_platform
    |----blueprints                 # 蓝图
         |----auth.py               # 用户注册登陆
         |----forms.py              # 表单验证
         |----questions_answer.py   # 问题发表回答+搜索
    |----migrations                 # 数据库迁移
    |----project_show               # 项目展示
    |----static                     # 静态资源
    |----templates                  # 前端模板
         |----base.heml             # 基础
         |----detail.html           # 问答展示
         |----index.html            # 首页
         |----login.html            # 注册
         |----public_question.html  # 问题展示
         |----register.html         # 注册
    |----app.py                     # 项目启动
    |----config.py                  # 配置文件
    |----decorrators.py             # 装饰器
    |----extend.py                  # 扩展，用于解决循环调用
    |----models.py                  # 数据库ORM模型
    |----README.md
    |----requirements.txt


## 项目简介
这是一个采用 python flask框架 + mysql数据库 搭建的简易问答平台。

## 如何使用
1.启动虚拟环境，安装相关依赖（终端运行）

    ./.venv/Scripts/activate

    pip install -r requirements.txt

2.创建数据库并修改 config.py 文件里面的配置信息

2.1 创建数据库（终端运行）

    mysql -u root -p
    create database your_database;

2.2 修改 config.py 配置文件

    USERNAME = 'your_name' # 修改为你的数据库用户
    PASSWORD = 'your_password' # 修改为你的数据库密码
    DATABASE = 'your_database' # 修改为你创建的数据库

    MAIL_USERNAME = 'your_email' # 修改为你的邮箱
    MAIL_PASSWORD = '<PASSWORD>' # 修改为你的邮箱授权码
    MAIL_DEFAULT_SENDER = 'your_email' # 修改为你的邮箱
注意：这里需要打开邮箱授权（用于发送验证码）

3.进行数据库迁移（终端执行）

    flask db init
    flask db migrate
    flask db upgrade
注意：flask db init 只需要执行一次

## 声明
该项目是一个学习 flask 的练习项目

该项目教程来源：https://space.bilibili.com/349929259

如果项目存在任何问题，可以参考该视频教程自己重新编码完成

非常感谢老师的免费教程