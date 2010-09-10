import os
from distutils.core import setup

def find_packages(root):
    # so we don't depend on setuptools; from the Storm ORM setup.py
    packages = []
    for directory, subdirectories, files in os.walk(root):
        if '__init__.py' in files:
            packages.append(directory.replace(os.sep, '.'))
    return packages

setup(
    name = 'django-tables',
    version = '0.2',
    description = 'Render QuerySets as tabular data in Django.',
    author = 'Kuba Janoszek (originally writen by Michael Elsdoerfer)',
    author_email = 'kuba.janoszek@gmail.com',
    license = 'BSD',
    url = 'http://github.com/jqb/django-tables',
    classifiers = [
        'Development Status :: 3 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
    packages = find_packages('django_tables'),
)
