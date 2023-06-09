from flask import render_template, flash, redirect, request, session 
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tip import Tip
from flask_app.models.test_result import Test_Result
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registration', methods=["POST"])
def register_new_user():
    if not User.validate_user_registration(request.form):
        return redirect('/')

    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }

    id = User.save(data)
    session["id"] = id
    return redirect('/welcome')

@app.route('/login', methods=["POST"])
def login():
    user_in_database = User.search_by_email(request.form)
    if not user_in_database: 
        flash("Invalid email/password")
        return redirect ('/')
        
    if not bcrypt.check_password_hash(user_in_database.password, request.form['password']):
        flash("Invalid email/password")
        return redirect ('/')
    session["id"] = user_in_database.id
    return redirect('/welcome_back')

@app.route('/welcome')
def welcome():
    if "id" not in session:
        return redirect('/logout/')

    return render_template("welcome.html", user = User.search_by_id({"id": session["id"]}), tips = Tip.get_one_random_tip())


@app.route('/welcome_back')
def welcomeback():
    if "id" not in session:
        return redirect('/logout')

    return render_template("welcomeback.html", user = User.search_by_id({"id": session["id"]}), test_results = Test_Result.get_scores_for_logged_in_user({"id": session["id"]}))



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')