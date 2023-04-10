from flask import render_template, redirect, request, session 
from flask_app import app
from flask_app.models.tip import Tip
from flask_app.models.user import User

@app.route('/advicecenter/edit', methods = ["POST"])
def edit_tip():
    Tip.edit(request.form)
    return redirect ('/advicecenter')


# If the user is not in session, they cannot delete the tip.

@app.route('/advicecenter/delete/<int:tip_id>')
def delete_tip(id):

    if "id" not in session:
        return redirect('/logout')

    data = {
        "id": id
    }

    tip = Tip.view_tip(id)

    if tip and tip.user == int(session["id"]):
        Tip.delete_tip(data)

    return redirect('/advicecenter')

