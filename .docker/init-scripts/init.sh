#!/bin/bash

psql -c "CREATE USER dev WITH CREATEDB PASSWORD 'dev';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE 'postgres' TO dev;"
psql -c "USER infisical WITH CREATEDB PASSWORD 'infisical';"
psql -c "create database infisical;"
psql -c "GRANT ALL PRIVILEGES ON DATABASE "postgres" TO infisical;"