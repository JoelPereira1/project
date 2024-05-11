"""Settings module for test app."""

host = 'localhost'
port = 5432
db_name = 'demo_postgres_app'
user = 'dev'
passwd = 'dev'

class Config:
  ENV = "test"
  TESTING = True
  SQLALCHEMY_DATABASE_URI = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"
  SECRET_KEY = "not-so-secret-in-tests"
  BCRYPT_LOG_ROUNDS = (
      4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
  )
  DEBUG_TB_ENABLED = False
  CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
  WTF_CSRF_ENABLED = False  # Allows form testing
  USE_REDIS = False
  USE_ES = False
  DATABASE_QUERY_TIMEOUT = 1000

  USE_REDIS = False
  REDIS_URL = 'redis://redis:6379'
  SQLALCHEMY_ECHO = True

  # SQLALCHEMY
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True
