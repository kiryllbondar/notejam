import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://notejamuser:FDFDd7837dsF@notejam-mysql.mysql.database.azure.com:3306/notejamdb' + os.path.join(basedir, 'notejam.db')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
