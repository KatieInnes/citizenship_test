from flask import render_template, redirect, request, session 
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tip import Tip


@app.route('/advice_center')
def all_tips(): 
    if "id" not in session:
        return redirect('/logout')

    return render_template("tips.html", user = User.search_by_id({"id": session["id"]}), advice = Tip.get_all_tips())


@app.route('/advice/new')
def create_tip():
    if "id" not in session:
        return redirect('/logout')

    return render_template("add_tip.html", user = User.search_by_id({"id": session["id"]}))


@app.route('/advice/new', methods=["POST"])
def save_new_tip():
    if not Tip.validate_tip(request.form):
        return redirect('/advice/new')

    if "id" not in session:
        return redirect('/')

    data = {
        "tip": request.form["tip"],
        "user_id": session["id"]
    }

    Tip.save_new_tip(data)
    return redirect('/advice_center')


@app.route('/advice/<int:id>')
def view_tip(id):

    data = {
        "id": id
    }
    return render_template("view_tip.html", tip=Tip.get_one_tip_by_id(data), logged_in_user = User.search_by_id({"id": session["id"]}))


@app.route('/advice/<int:id>/edit')
def edit_tip(id):

    if "id" not in session:
        return redirect('/logout')
    
    data = {
        "id": id
    }

    tip = Tip.get_one_tip_by_id(data)

    if tip and tip.user_id == int(session["id"]):
        return render_template("edit_tip.html", tip=Tip.get_one_tip_by_id(data)) 

    return redirect("/advice_center")


@app.route('/advice/<int:id>/edit', methods=["POST"])
def update_tip(id):
    if not Tip.validate_tip(request.form):
        return redirect(f"/advice/{id}/edit")

    data = {
        "id": request.form["id"],
        "tip": request.form["tip"]
        }

    Tip.update_tip(data)
    return redirect('/advice_center')


@app.route('/advice/<int:id>/delete')
def delete_tip(id):

    if "id" not in session:
        return redirect('/logout')

    data = {
        "id": id
    }

    tip = Tip.get_one_tip_by_id(data)

    if tip and tip.user_id == int(session["id"]):
        Tip.delete_tip(data)

    return redirect('/advice_center')

