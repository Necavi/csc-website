from flask import Flask

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile("settings.py")

db = SQLAlchemy(app)


def run(*args, **kwargs):
    app.jinja_env.auto_reload = True
    app.jinja_env.add_extension("jinja2.ext.loopcontrols")

    login_manager = LoginManager()
    login_manager.init_app(app)

    from . import models

    db.drop_all()

    db.create_all()

    from . import load_data

    from . import routes
    from . import jinja_context

    app.run(*args, **kwargs)
