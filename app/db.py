from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure_database(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
