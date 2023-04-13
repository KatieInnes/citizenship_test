from flask import render_template, redirect, request, session 
from flask_app import app
from flask_app.models.question_answer import QuestionAnswer

# @app.route('/test')
# def question():
#     if "id" not in session:
#         return redirect('/logout/')

#     my_questions = QuestionAnswer.get_ten_questions()
#     return render_template("question.html", questions = my_questions)



@app.route('/question/<int:page_id>')
def question():
    if "id" not in session:
        return redirect('/logout/')

    if "page_id" is 1:
        session['answers'] = [];
        session['questions'] = QuestionAnswer.get_ten_questions();

    my_questions = session['questions']
    return render_template("question.html", question_number_page=page_id, questions = my_questions[id])



@app.route('/question/<int:page_id>', methods=["POST"])
def answer_question(id):

    answer_array = session['answers'];
    answer_array.push(answer_form);
    session['answers'] = answer_array;
    

    # if "page_id" == 10;
    #     return redirect('/results')
    # else
    return redirect('/question/{page_id+1}')

# @app.route('/answers')
# def view_sighting(id):

#     answer_array = session['answers'];
#     answer_array.count(true)