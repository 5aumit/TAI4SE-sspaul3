import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

# CHECK IF PRODUCTION CONFIG EXISTS
if os.path.exists('/etc/config.json'):
    with open('/etc/config.json') as config_file:
        config = json.load(config_file)
else:
    with open('dev_config.json') as config_file:
        config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = config.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(config.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = config.get('MAIL_SUBJECT_PREFIX')
    MAIL_SENDER = config.get('MAIL_SENDER')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '../data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
