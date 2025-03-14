

# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'your_name' # 修改为你的数据库用户
PASSWORD = 'your_password' # 修改为你的数据库密码
DATABASE = 'your_database' # 修改为你创建的数据库
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE) # 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USERNAME = 'your_email' # 修改为你的邮箱
MAIL_PASSWORD = '<PASSWORD>' # 修改为你的邮箱授权码
MAIL_DEFAULT_SENDER = 'your_email' # 修改为你的邮箱
MAIL_USE_SSL = True

# session加密的secret_key
SECRET_KEY = 'secretkey'