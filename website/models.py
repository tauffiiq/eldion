from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Perawat(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    alamat = db.Column(db.String(500))
    telfon = db.Column(db.String(50))
    foto = db.Column(db.String(50))

# class Bio(db.Model) :
#     id = db.Column(db.integer, promary_key=True)
#     name = db.Column(db.String(150))