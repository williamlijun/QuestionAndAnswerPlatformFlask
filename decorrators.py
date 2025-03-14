from functools import wraps
from flask import g, redirect, url_for

# 装饰器
# f是一个函数
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('auth.login')) # 用户没有登陆
        else:
            return f(*args, **kwargs) # 保留当前参数，并继续执行f函数
    return wrap # 返回登陆界面或者返回当前正在执行的函数f