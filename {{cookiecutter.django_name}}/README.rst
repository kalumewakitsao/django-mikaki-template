{{ cookiecutter.project_name }} README
--------------------------------------

Packaging
---------
1. Add an entry to CHANGELOG bumping the version number.
2. Change the version number in ``setup.py`` to concur with the one in CHANGELOG.
3. Run ``python setup.py sdist bdist_wheel`` on the root dir to generate the package

useful links:
https://stackoverflow.com/questions/15031694/installing-python-packages-from-local-file-system-folder-to-virtualenv-with-pip
https://packaging.python.org/tutorials/packaging-projects/


copyright {{ cookiecutter.company_name }}
release date: {{ cookiecutter.release_date }}
year: {{ cookiecutter.year }}