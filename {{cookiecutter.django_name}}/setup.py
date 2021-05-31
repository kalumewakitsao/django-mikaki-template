import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='{{ cookiecutter.project_name }}',
    version='{{ cookiecutter.version }}',
    packages=find_packages(),
    include_package_data=True,
    license='{{ cookiecutter.project_name }} License',
    description='{{ cookiecutter.project_description }}',
    long_description=README,
    url='{{ cookiecutter.project_url }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIKAKI License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'dj-database-url',
        'Django==3.2',
        'ipython',
        'djangorestframework',
        'django-extensions',
        'django-filter',
        'psycopg2-binary',
    ],
    python_requires='>=3.7',
)
