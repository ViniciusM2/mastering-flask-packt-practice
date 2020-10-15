class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    HOST = '0.0.0.0'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
