from flask import Flask, session, render_template, redirect, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from Db import db
from Db.models import


app = Flask(__name__)


app.secret_key = 'tooth'  # Ключ для сессий
user_db = "karina"
host_ip = "127.0.0.1"
host_port = "5432"
database_name = "initiatives"
password = "davo"


app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
