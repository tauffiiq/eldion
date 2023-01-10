from audioop import add
from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/perawat")
@login_required
def perawat():
    return render_template("perawat.html", user=current_user)

@views.route("/bio", methods=['GET', 'POST'])
@login_required
def bio():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        alamat = request.form.get('alamat')
        telfon = request.form.get('telfon')
        
        add_data = add(alamat, telfon)
        db.session.add(add_data)
        db.session.commit()
        
        return print(alamat, telfon)


    return render_template("bio.html", user=current_user)
