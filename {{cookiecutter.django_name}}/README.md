
# {{ cookiecutter.project_name|upper }} Title

{{ cookiecutter.project_description }}


## Installation 

The project runs on `python 3.7` or later, best run on a [`virtual environment`](https://virtualenv.pypa.io/en/latest/), and also is configured based on the `postgresql` database management system.
Following is a step by step guide on how to install the project and dependencies.

```bash
  # ensure you have a working installation of postgresql
  psql postgres (mac users)

  # create the databases, templates can be found under database.sql.
  # run these sql  commands in the psql shell
  CREATE DATABASE {{ cookiecutter.project_name }} WITH OWNER postgres;
  GRANT ALL PRIVILEGES ON DATABASE {{ cookiecutter.project_name }} TO app;

  # install virtualenv using pip, some configurations might be needed
  python -m pip install --user virtualenv

  # create the virtualenv
  virtualenv -p python3.7[.8, .9]

  # install requirements
  pip install -r requirements/base.txt

  # run database migrations
  python manage.py migrate

  # run the server
  python manage.py runserver
```

    
## Running Tests

To run tests, run the following command

```bash
  # ensure you have tox installed
  pip install tox

  # then run tests
  tox
```

By default, tests will be run against multiple versions of python for compatibility.


The project is also configured to run tests on `Github Actions` to ensure that you do the minimal to be up and running.


## Packaging

1. Add an entry to CHANGELOG bumping the version number.
2. Change the version number in ``setup.py`` to concur with the one in CHANGELOG.
3. Run ``python setup.py sdist bdist_wheel`` on the root dir to generate the package

  
## Authors

- [@{{ cookiecutter.company_name }}](https://www.github.com/{{ cookiecutter.company_name }})

useful links:
https://stackoverflow.com/questions/15031694/installing-python-packages-from-local-file-system-folder-to-virtualenv-with-pip
https://packaging.python.org/tutorials/packaging-projects/


copyright {{ cookiecutter.company_name }}
release date: {{ cookiecutter.release_date }}
year: {{ cookiecutter.year }}