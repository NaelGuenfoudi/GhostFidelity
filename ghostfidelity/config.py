# Global configuration settings
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'ghostfidelity.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
