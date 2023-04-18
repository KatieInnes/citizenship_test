from flask import render_template, redirect, session, request 
from flask_app import app
from flask_app.models.question_answer import QuestionAnswer
from flask_app.models.test_result import Test_Result

@app.route('/question/<int:page_id>')
def question(page_id):
    # if not QuestionAnswer.selection_required(request.form)

    if "id" not in session:
        return redirect('/logout/')

    if page_id == 0:
        session['answers'] = [];
        session['questions'] = QuestionAnswer.get_ten_questions();

    my_questions = session['questions']
    answer_array = session['answers']

    return render_template("question.html", question_number_page=page_id, question = my_questions[page_id], answer_array=answer_array)


@app.route('/question/<int:page_id>', methods=["POST"])
def answer_question(page_id):

    answer_array = session['answers']
    if request.form["answer"] == "true":
        answer_array.append(1)
    else:
        answer_array.append(0)
    session["answers"] = answer_array;

    if page_id == 9:
        data = {
            "score": answer_array.count(1),
            "user_id": session["id"]
        }
        Test_Result.save_new_score(data)
        return redirect('/results')
    else:
        next_page = int(page_id) + 1
        return redirect('/question/' + str(next_page))
