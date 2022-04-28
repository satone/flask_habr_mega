import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-can-tell'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'korjkx.ru'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'noreply@korjkx.ru'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'noreply@korjkx.ru'
    ADMINS = ['pdm@korjkx.ru']

    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'ru']

    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
