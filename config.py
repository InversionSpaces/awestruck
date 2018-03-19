import os

basedir = os.getcwd()

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS = True
