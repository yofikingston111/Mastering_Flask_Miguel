import os
basedir = os.path.abspath(os.path.dirname(__file__))

#class congfig
class Config(object):
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost/UserDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


