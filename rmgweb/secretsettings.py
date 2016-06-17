import os.path
from rmgpy import settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# The website administrators
ADMINS = [
    ('Richard West', 'R.West@northeastern.edu')
    # ('Your Name', 'your_email@domain.com'),
]

# The full path of the Django project (as determined from the location of this file)
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# The path to the RMG-database project
DATABASE_PATH = settings['database.directory']

# Configuration of the database backend
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',                 # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, 'sqlitedb', 'combined.db'),        # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Place your secret key here.
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i+a0dzd@buc8k!4#(zn!*h#f4iinp*_v@6cu!08u_3^uwbzwp#'
