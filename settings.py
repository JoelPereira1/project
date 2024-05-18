# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from pathlib import Path
from flask.helpers import get_debug_flag
from infisical import InfisicalClient
from infisical_client import ClientSettings, InfisicalClient, GetSecretOptions, ListSecretsOptions

# WORK ON LOCAL ENV WITH DOCKER AND INFISICAL FROM PROJ
if os.environ.get("APP_ENV") == 'local':
  # VALUES
  secretkeyvalue = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
  dbtypekeyvalue = 'postgresql'
  dbhostkeyvalue = 'localhost'
  dbportkeyvalue = 5432
  dbnamekeyvalue = 'demo_postgres_app'
  dbuserkeyvalue = 'dev'
  dbpasswdkeyvalue = 'dev'
  redisurikeyvalue = 'redis://redis:6379'
  miniohostvalue = 'localhost'
  minioportvalue = '9000'
  miniokeyvalue = 'rq7AynI9TVrzBxUFZGvn'
  miniosecretvalue = 'zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG'
  miniobucketvalue = 'flowershop'
  rethinkhostvalue = 'localhost'
  rethinkportvalue = 28015
  rethinkbdvalue = 'flask_chat'
  rethinkpassvalue = 'Passw0rd!'
  rethinktablevalue = 'tblchat'
else:
  if os.environ.get("APP_ENV1") == 'local':
    # client = InfisicalClient(token="st.6be0fef8-8728-433c-b9b6-3041628dd126.bb9915efe35c4db3d98136f9cece621a.7fae5b93bdcb8c6e45a088fdf47aba87")
    client = InfisicalClient(ClientSettings(
      site_url='http://localhost:9090',
      client_id='d1b18a21-72e3-4e01-8548-9f913dcb7121',
      client_secret='e795dcce1c2180114ccd72c8d9e8d7c94522e3859018a80f4ced63e471bf9c57'#,
      # access_token="st.6be0fef8-8728-433c-b9b6-3041628dd126.bb9915efe35c4db3d98136f9cece621a.7fae5b93bdcb8c6e45a088fdf47aba87"
    ))
    client.listSecrets(options=ListSecretsOptions(
      environment='dev',
      project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70'
    ))
  else:
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
  # SHOP
  secretkey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='SECRET_KEY'
  ))
  # DB
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
  # REDIS
  redisurikey = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='REDIS_URI'
  ))
  # MINIO
  miniohost = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='MINIO_HOST'
  ))
  minioport = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='MINIO_PORT'
  ))
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
  miniobucket = client.getSecret(options=GetSecretOptions(
    environment='dev',
    project_id='2da2b9ce-8d10-4d3e-95c4-947404b34a70',
    secret_name='MINIO_BUCKET'
  ))
  # RETHINK
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

  # VALUES
  secretkeyvalue = secretkey.secret_value
  dbtypekeyvalue = dbtypekey.secret_value
  dbhostkeyvalue = dbhostkey.secret_value
  dbportkeyvalue = dbportkey.secret_value
  dbnamekeyvalue = dbnamekey.secret_value
  dbuserkeyvalue = dbuserkey.secret_value
  dbpasswdkeyvalue = dbpasswdkey.secret_value
  redisurikeyvalue = redisurikey.secret_value
  miniohostvalue = miniohost.secret_value
  minioportvalue = minioport.secret_value
  miniokeyvalue = miniokey.secret_value
  miniosecretvalue = miniosecret.secret_value
  miniobucketvalue = miniobucket.secret_value
  rethinkhostvalue = rethinkhost.secret_value
  rethinkportvalue = rethinkport.secret_value
  rethinkbdvalue = rethinkbd.secret_value
  rethinkpassvalue = rethinkpass.secret_value
  rethinktablevalue = rethinktable.secret_value

# access_key="", secret_key="")
# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# print(dbtypekey.secret_value) # postgresql
# print(dbhostkey.secret_value) # postgres
# print(dbportkey.secret_value) # 5432
# print(dbnamekey.secret_value) # demo_postgres_app
# print(dbuserkey.secret_value) # dev
# print(dbpasswdkey.secret_value) # dev
# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# print('###########################################################################################################')
# print(redisurikey.secret_value) # redis://redis:6379
# print(secret_key.secret_value) # tO$&!|0wkamvVia0?n$NqIRVWOG
# print('###########################################################################################################')
# print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
# print(miniohost.secret_value) # minio
# print(minioport.secret_value) # 9000
# print(miniokey.secret_value) # rq7AynI9TVrzBxUFZGvn
# print(miniosecret.secret_value) # zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG
# print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
# print('////////////////////////////////////////////////////////////////////////////////////////////////////////////')
# print(rethinkhost.secret_value) # rethinkdb
# print(rethinkport.secret_value) # 28015
# print(rethinkbd.secret_value) # flask_chat
# print(rethinkpass.secret_value) # Passw0rd!
# print(rethinktable.secret_value) # tblchat
# print('/////////////////////////////////////////////////////////////////////////////////////////////////////////')

class DBConfig:
  db_type = os.getenv("DB_TYPE", dbtypekeyvalue)
  host = os.getenv("DB_HOST", dbhostkeyvalue)
  port = os.getenv("DB_PORT", dbportkeyvalue)
  db_name = os.getenv("DB_NAME", dbnamekeyvalue)
  user = os.getenv("DB_USER", dbuserkeyvalue)
  passwd = os.getenv("DB_PASSWD", dbpasswdkeyvalue)
  if db_type == "postgresql":
    db_uri = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"
  elif db_type == "mysql":
    db_uri = (
      f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8mb4"
    )
  redis_uri = redisurikeyvalue
  rethinkdb_uri = os.getenv("RETHINKHOST", rethinkhostvalue)
  rethinkdb_port = os.getenv("RETHINKPORT", rethinkportvalue)
  rethinkdb = os.getenv("RETHINKDB", rethinkbdvalue)
  rethinkdb_pwd = os.getenv("RETHINKPASS", rethinkpassvalue)
  rethinkdb_tbl = os.getenv("RETHINKTABLE", rethinktablevalue)
  esearch_uri = "localhost"

class Config:
  ENV = "dev"
  FLASK_DEBUG = get_debug_flag()
  SECRET_KEY = os.getenv('SECRET_KEY', secretkeyvalue)
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
  # MINIO_URL	Hostname of a S3 service.	-
  MINIO_API_HOST = os.getenv('MINIO_HOST', miniohostvalue)
  MINIO_API_PORT = os.getenv('MINIO_PORT', minioportvalue)
  MINIO_API_URI = os.getenv('MINIO_URI', f"{miniohostvalue}:{minioportvalue}")
  MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', miniokeyvalue) 	#(Optional) Access key (aka user ID) of your account in S3 service.	-
  MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', miniosecretvalue) 	#(Optional) Secret Key (aka password) of your account in S3 service.	-
  BUCKET_NAME = os.getenv('MINIO_BUCKET', miniobucketvalue)
  # MINIO_SESSION_TOKEN	(Optional) Session token of your account in S3 service.	-
  # MINIO_SECURE_CONNECTION	(Optional) Flag to indicate to use secure (TLS) connection to S3 service or not.	False
  # MINIO_REGION	(Optional) Region name of buckets in S3 service.	-
  # MINIO_HTTP_CLIENT	(Optional) Customized HTTP client.	-
  # MINIO_CREDENTIALS	(Optional) Credentials of your account in S3 service.	-
  # MINIO_BUCKETS	(Optional) A list of buckets, that should be created at startup	-
