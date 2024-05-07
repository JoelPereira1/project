# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from pathlib import Path
from flask.helpers import get_debug_flag
from infisical import InfisicalClient
from infisical_client import ClientSettings, InfisicalClient, GetSecretOptions, ListSecretsOptions

# client = InfisicalClient(token="st.6be0fef8-8728-433c-b9b6-3041628dd126.bb9915efe35c4db3d98136f9cece621a.7fae5b93bdcb8c6e45a088fdf47aba87")
client = InfisicalClient(ClientSettings(
    site_url='http://infisical-backend:8080',
    client_id='d1b18a21-72e3-4e01-8548-9f913dcb7121',
    client_secret='e795dcce1c2180114ccd72c8d9e8d7c94522e3859018a80f4ced63e471bf9c57'#,
    # access_token="st.6be0fef8-8728-433c-b9b6-3041628dd126.bb9915efe35c4db3d98136f9cece621a.7fae5b93bdcb8c6e45a088fdf47aba87"
))
client.listSecrets(options=ListSecretsOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70'
))
dbtypekey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='DB_TYPE'
))
dbhostkey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='DB_HOST'
))
dbportkey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='DB_PORT'
))
dbnamekey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='DB_NAME'
))
dbuserkey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='DB_USER'
))
dbpasswdkey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='DB_PASSWD'
))

# dbtypekey = client.get_secret("DB_TYPE")
# dbhostkey = client.get_secret("DB_HOST")
# dbnamekey = client.get_secret("DB_NAME")
# dbuserkey = client.get_secret("DB_USER")
# dbpasswdkey = client.get_secret("DB_PASSWD")
# dbportkey = client.get_secret("DB_PORT")

# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# print(dbtypekey.secret_value) # postgresql
# print(dbhostkey.secret_value) # postgres
# print(dbportkey.secret_value) # 5432
# print(dbnamekey.secret_value) # demo_postgres_app
# print(dbuserkey.secret_value) # dev
# print(dbpasswdkey.secret_value) # dev
# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

redisurikey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='REDIS_URI'
))

secret_key = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='SECRET_KEY'
))
# print('###########################################################################################################')
# print(redisurikey.secret_value) # redis://redis:6379
# print(secret_key.secret_value) # tO$&!|0wkamvVia0?n$NqIRVWOG
# print('###########################################################################################################')

miniokey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='MINIO_KEY'
))

miniosecret = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='MINIO_SECRET'
))
# print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
# print(miniokey.secret_value) # redis://redis:6379
# print(miniosecret.secret_value) # tO$&!|0wkamvVia0?n$NqIRVWOG
# print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


rethinkhost = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='RETHINKHOST'
))
rethinkport = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='RETHINKPORT'
))
rethinkbd = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='RETHINKDB'
))
rethinkpass = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='RETHINKPASS'
))
rethinktable = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='RETHINKTABLE'
))

# print('////////////////////////////////////////////////////////////////////////////////////////////////////////////')
# print(rethinkhost.secret_value) # rethinkdb
# print(rethinkport.secret_value) # 28015
# print(rethinkbd.secret_value) # flask_chat
# print(rethinkpass.secret_value) # Passw0rd!
# print(rethinktable.secret_value) # tblchat
# print('/////////////////////////////////////////////////////////////////////////////////////////////////////////')

miniokey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='MINIO_KEY'
))
miniosecret = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='MINIO_SECRET'
))

class DBConfig:
  db_type = os.getenv("DB_TYPE", dbtypekey.secret_value)
  host = os.getenv("DB_HOST", dbhostkey.secret_value)
  port = os.getenv("DB_PORT", dbportkey.secret_value)
  db_name = os.getenv("DB_NAME", dbnamekey.secret_value)
  user = os.getenv("DB_USER", dbuserkey.secret_value)
  passwd = os.getenv("DB_PASSWD", dbpasswdkey.secret_value)
  # db_type = os.getenv("DB_TYPE", 'postgresql')
  # host = os.getenv("DB_HOST", 'localhost')
  # port = os.getenv("DB_PORT", 5432)
  # db_name = os.getenv("DB_NAME", 'flask_app')
  # user = os.getenv("DB_USER", 'dev')
  # passwd = os.getenv("DB_PASSWD", 'dev')
  if db_type == "postgresql":
    db_uri = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"
  elif db_type == "mysql":
    db_uri = (
      f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8mb4"
    )
  redis_uri = redisurikey.secret_value #"redis://redis:6379"
  # redis_uri = "redis://redis:6379"
  esearch_uri = "localhost"

  rethinkdb_uri = os.getenv("RETHINKHOST", rethinkhost.secret_value)
  rethinkdb_port = os.getenv("RETHINKPORT", rethinkport.secret_value)
  rethinkdb = os.getenv("RETHINKDB", rethinkbd.secret_value)
  rethinkdb_pwd = os.getenv("RETHINKPASS", rethinkpass.secret_value)
  rethinkdb_tbl = os.getenv("RETHINKTABLE", rethinktable.secret_value)

class Config:
  ENV = "dev"
  FLASK_DEBUG = get_debug_flag()
  SECRET_KEY = os.getenv('SECRET_KEY', secret_key.secret_value) #tO$&!|0wkamvVia0?n$NqIRVWOG
  # SECRET_KEY = os.getenv('SECRET_KEY', 'tO$&!|0wkamvVia0?n$NqIRVWOG')
  WTF_CSRF_ENABLED = False  # Allows form testing
  # Redis
  # if redis is enabled, it can be used for:
  #   - cache
  #   - save product description
  #   - save page content
  USE_REDIS = os.getenv('USE_REDIS', False)
  REDIS_URL = os.getenv('REDIS_URI', DBConfig.redis_uri)
  SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO', True)

  # SQLALCHEMY
  SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", DBConfig.db_uri)
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  DATABASE_QUERY_TIMEOUT = 0.1  # log the slow database query, and unit is second
  SQLALCHEMY_RECORD_QUERIES = True

  # Dir
  APP_DIR = Path(__file__).parent # This directory
  PROJECT_ROOT = APP_DIR.parent
  STATIC_DIR = APP_DIR / 'shop' / 'static'

  UPLOAD_FOLDER = ''
  UPLOAD_DIR = STATIC_DIR / UPLOAD_FOLDER
  DASHBOARD_TEMPLATE_FOLDER = APP_DIR / 'shop' / 'templates' / 'dashboard'
  UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "shop/static/placeholders")

  PURCHASE_URI = os.getenv("PURCHASE_URI", "")

  BCRYPT_LOG_ROUNDS = 13
  DEBUG_TB_ENABLED = get_debug_flag()
  DEBUG_TB_INTERCEPT_REDIRECTS = False

  MESSAGE_QUOTA = 10

  MAIL_SERVER = os.getenv("MAIL_SERVER", "localhost")
  MAIL_PORT = os.getenv("MAIL_PORT", 25)
  MAIL_TLS = os.getenv("MAIL_TLS", False)
  MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
  MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")

  GA_MEASUREMENT_ID = os.getenv("GA_MEASUREMENT_ID", "")

  # minio
  # access_key="rq7AynI9TVrzBxUFZGvn", secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG")
  # MINIO_URL	Hostname of a S3 service.	-
  MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', miniokey.secret_value) 	#(Optional) Access key (aka user ID) of your account in S3 service.	-
  MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', miniosecret.secret_value) 	#(Optional) Secret Key (aka password) of your account in S3 service.	-
  # MINIO_SESSION_TOKEN	(Optional) Session token of your account in S3 service.	-
  # MINIO_SECURE_CONNECTION	(Optional) Flag to indicate to use secure (TLS) connection to S3 service or not.	False
  # MINIO_REGION	(Optional) Region name of buckets in S3 service.	-
  # MINIO_HTTP_CLIENT	(Optional) Customized HTTP client.	-
  # MINIO_CREDENTIALS	(Optional) Credentials of your account in S3 service.	-
  # MINIO_BUCKETS	(Optional) A list of buckets, that should be created at startup	-


