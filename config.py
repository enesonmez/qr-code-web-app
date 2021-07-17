import os


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = ""


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG=True
    SECRET_KEY = "secret_for_test_environment"