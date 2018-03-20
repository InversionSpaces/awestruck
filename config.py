import os

basedir = os.getcwd()

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = False

SECRET_KEY = "5ebe2294ecd0e0f08eab7690d2a6ee69"
