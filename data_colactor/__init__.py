from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    if 'DATABASE_URL' in os.environ:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

    if 'SECRET_KEY' in os.environ:
        app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
    else:
        app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Data

    return app
