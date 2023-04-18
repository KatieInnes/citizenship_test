from flask import render_template, redirect, session 
from flask_app import app
from flask_app.models.test_result import Test_Result
from flask_app.models.user import User


@app.route('/results')
def results():
    if "id" not in session:
        return redirect('/logout/')


    return render_template("results.html", test_result = Test_Result.most_recent_score_for_logged_in_user({"id": session["id"]})[0], test_results = Test_Result.get_scores_for_logged_in_user({"id": session["id"]}))