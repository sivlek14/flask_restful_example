class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1164543@172.17.0.2/flask_restful"
	SECRET_KEY = '6468202b-463a-4c7e-88f1-a97987a75ecd'

class ProductionConfig(Config):
	DEBUG = False

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(Config):
	TESTING = True