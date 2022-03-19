import os

#secret key configuration
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youl-will-never-guess'
