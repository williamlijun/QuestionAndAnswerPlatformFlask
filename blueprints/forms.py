import wtforms
from wtforms.validators import Email, length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from extend import db

# Email：email_validator

class RegistrationForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    captcha = wtforms.StringField(validators=[length(min=6, max=6, message="验证码格式错误")])
    username = wtforms.StringField(validators=[length(min=3, max=20, message="用户名格式错误")])
    password = wtforms.StringField(validators=[length(min=6, max=20, message="密码格式错误")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="两次密码不一致")])

    def validate_email(self, field):
        user = UserModel.query.filter_by(email=field.data).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册")

    def validate_captcha(self, field):
        captcha_email = EmailCaptchaModel.query.filter_by(email=self.email.data, captcha_token=field.data).first()
        if not captcha_email:
            raise wtforms.ValidationError(message="邮箱或验证码错误")
        else: # 验证成功后删除验证码记录
            db.session.delete(captcha_email)
            db.session.commit()

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    password = wtforms.StringField(validators=[length(min=6, max=20, message="密码格式错误")])

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=3, max=100, message="标题格式错误")])
    content = wtforms.StringField(validators=[length(min=3, message="内容格式错误")])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=3, message="内容格式错误")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须传入问题id")])