from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from extend import mail, db
from flask_mail import Message
from flask import request
import string
import random
from models import UserModel, EmailCaptchaModel
from blueprints.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id # flask中的session，是经过加密后存储在cookie中的
                return redirect(url_for("question_answer.index"))
            else:
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    # 表单验证：flask-wtf
    else:
        form = RegistrationForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password)) # generate_password_hash 加密密码
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.register'))

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('question_answer.index'))

# @auth_bp.route('/mail/test')
# def mail_test():
#     message = Message(subject='test', recipients=['1021074702@qq.com'], body='test')
#     mail.send(message)
#     return "邮件发送成功"

# 未指定方法，默认get
@auth_bp.route('/captcha/email')
def captcha_email():
    # /captcha/email/<email> 路由形式
    # /captcha/email?email=xxx 字符串形式
    email = request.args.get('email')
    source = string.ascii_letters + string.digits + string.punctuation # 构建验证的字符串池
    captcha_token = ''.join(random.sample(source, 6)) # 从字符串池里面随机取6个生成验证码
    message = Message(subject="flask 问答平台验证码", recipients=[email], body=f"您的flask问答平台验证码是:'{captcha_token}'")
    mail.send(message)
    # 存储验证码-缓存：memcached/redis
    # 用数据库存储
    email_captcha = EmailCaptchaModel(email=email, captcha_token=captcha_token)
    db.session.add(email_captcha)
    db.session.commit()

    return jsonify({"code": 200, "message": "", "data": None})