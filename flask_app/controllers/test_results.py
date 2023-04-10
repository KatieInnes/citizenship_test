from flask import render_template, redirect, request, session 
from flask_app import app
from flask_app.models.test_result import Test_Result
from flask_app.models.user import User

@app.route('/welcome')
def welcome():
    if "id" not in session:
        return redirect('/logout')
    data = {
        "id": session["id"]
    }
    return render_template("welcome.html")
