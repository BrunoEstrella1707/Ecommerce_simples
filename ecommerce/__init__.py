from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"
app.config["SECRET_KEY"] = '77d14c70a72c25c6bedfbe88'
db.init_app(app)

from ecommerce import routes
