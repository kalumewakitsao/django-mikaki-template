DROP USER IF EXISTS app;

CREATE USER app WITH CREATEDB CREATEROLE SUPERUSER LOGIN PASSWORD 'app';

DROP DATABASE IF EXISTS {{ cookiecutter.project_name }};

CREATE DATABASE {{ cookiecutter.project_name }} WITH OWNER postgres;
GRANT ALL PRIVILEGES ON DATABASE {{ cookiecutter.project_name }} TO app;