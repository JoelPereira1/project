CREATE USER dev WITH CREATEDB PASSWORD 'dev';
GRANT ALL PRIVILEGES ON DATABASE "postgres" TO dev;
CREATE USER infisical WITH CREATEDB PASSWORD 'infisical';
create database infisical;
GRANT ALL PRIVILEGES ON DATABASE "postgres" TO infisical;
