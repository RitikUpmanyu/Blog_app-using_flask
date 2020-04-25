import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['ritikup008@gmail.com']
    POSTS_PER_PAGE = 12
    LANGUAGES = ['en','es','hi']
    YANDEX_TRANSLATOR_KEY = os.environ.get('YANDEX_TRANSLATOR_KEY')
    MAX_CONTENT_LENGTH = 4 * 1024 * 1024
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
#  pybabel extract -F babel.cfg -o messages.pot --input-dirs=.   this command is for making .pot file for translations
