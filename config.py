# All configs should be uppercase
import os


basedir = os.path.abspath(os.path.dirname(__file__))


if os.environ.get('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')

# Turn off the Flask-SQLAlchemy event system
SQLALCHEMY_TRACK_MODIFICATIONS = False
