
class DevelopmentConfig:
  SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Mahirane231995@localhost/Bank'

  DEBUG = True #cause debugging for any changes you make  
  CACHE_TYPE = 'SimpleCache'
  CACHE_DEFAULT_TIMEOUT = 300

class TestingConfig:
  pass

class ProductionConfig:
  pass
