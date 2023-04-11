from flask import render_template, redirect, request, session 
from flask_app import app
from flask_app.models.question_answer import QuestionAnswer

@app.route('/test')
def question():
    if "id" not in session:
        return redirect('/logout/')

    my_questions = QuestionAnswer.get_ten_questions()
    return render_template("question.html", questions = my_questions)