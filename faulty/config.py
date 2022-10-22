import os


class Config(object):
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    BOOTSTRAP_SERVE_LOCAL = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
