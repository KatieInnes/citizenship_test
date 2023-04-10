from flask import render_template, redirect, request, session 
from flask_app import app
from flask_app.models.tip import Tip
from flask_app.models.user import User

@app.route('/advicecenter/edit', methods = ["POST"])
def edit():
    Tip.edit(request.form)
    return redirect ('/advicecenter')


@app.route('/advicecenter/delete/<int:tip_id>')
def delete(tip_id):
    Tip.delete(tip_id)
    return redirect('/advicecenter')
