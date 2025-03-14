from flask import Flask, session, g
import config
from extend import db, mail
from models import UserModel
from blueprints.auth import auth_bp
from blueprints.question_answer import question_answer_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config) # 导入配置文件

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db) # 数据库迁移
# flask db init 只需要执行一次
# flask db migrate 将orm模型生成迁移脚本
# flask db upgrade 将迁移脚本映射到数据库

app.register_blueprint(auth_bp) # 绑定蓝图
app.register_blueprint(question_answer_bp) # 绑定蓝图

# 钩子函数：before_request/ before_first_request/ after_request
@app.before_request
def before_request():
    user_id = session.get('user_id') # flask自动进行解密
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,"user", user)
    else:
        setattr(g,"user",None)

# 上下文处理器
@app.context_processor
def inject_user():
    return dict(user=g.user) # 在所有模板都可以使用


if __name__ == '__main__':
    app.run(debug=True)
