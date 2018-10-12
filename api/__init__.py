import os

from flask import Flask, request
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_utils import create_database, database_exists
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from api.config import config

def create_app(test_config=None):
    app = Flask(__name__)

    # check environment variables to see which config to load
    env = os.environ.get("FLASK_ENV", "dev")
    if test_config:
        # ignore environment variable config if config was given
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(config[env])


    # decide whether to create database
    if env != "prod":
        db_url = app.config["SQLALCHEMY_DATABASE_URI"]
        if not database_exists(db_url):
            create_database(db_url)

    bootstrap = Bootstrap(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # register sqlalchemy to this app
    from api.models import db

    db.init_app(app)
    Migrate(app, db)

    # import and register blueprints
    from api.views import main

    app.register_blueprint(main.main)

    return app
