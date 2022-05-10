import os
basedir = os.path.abspath(os.path.dirname(__file__))

#class congfig
class Config(object):
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost/UserDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "powerful secretkey",
    WTF_CSRF_SECRET_KEY = "a csrf secret key"

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['fery@gmail.com']

    POSTS_PER_PAGE = 3
