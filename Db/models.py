from . import db
from sqlalchemy import func


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)


class initiatives(db.Model):
    initiatives_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    rating = db.Column(db.Integer, default=0)