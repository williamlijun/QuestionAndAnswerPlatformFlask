from flask import Blueprint, request, render_template, g, url_for, redirect
from blueprints.forms import QuestionForm, AnswerForm
from models import QuestionModel, AnswerModel
from extend import db
from decorrators import login_required

question_answer_bp = Blueprint('question_answer', __name__, url_prefix='/')


# http://127.0.0.1:5000
@question_answer_bp.route('/')
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template('index.html', questions=questions)

@question_answer_bp.route('/question_answer/question/public',methods=['GET','POST'])
@login_required # 装饰器，在执行下面的函数之前进行处理，调用login_required.login_required(f)，进行用户是否登陆的判断，这里的f=public_question()
def public_question():
    if request.method == 'GET':
        return render_template("public_question.html")
    elif request.method == 'POST':
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('question_answer.index'))
        else:
            return redirect(url_for('question_answer.public_question'))

@question_answer_bp.route('/question_answer/detail/<int:question_id>',methods=['GET','POST'])
def detail_question(question_id):
    question = QuestionModel.query.get_or_404(question_id)
    return render_template("detail.html", question=question)

@question_answer_bp.route('/question_answer/answer/public',methods=['POST'])
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content, author_id=g.user.id, question_id=question_id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('question_answer.detail_question', question_id=question_id))
    else:
        return redirect(url_for('question_answer.detail_question', question_id=request.args.get('question_id')))

@question_answer_bp.route('/question_answer/question/search',methods=['GET','POST'])
def search_question():
    # /search?q=xxx
    # /search/<question>
    # post, request.form
    question = request.args.get('question')
    questions = QuestionModel.query.filter(QuestionModel.title.contains(question)).all()
    return render_template('index.html', questions=questions)