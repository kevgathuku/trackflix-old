# All configs should be uppercase
import os

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)

if not SQLALCHEMY_DATABASE_URI:
    raise Exception("DATABASE_URL missing")

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')

# Turn off the Flask-SQLAlchemy event system
SQLALCHEMY_TRACK_MODIFICATIONS = False
