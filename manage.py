from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import app, db


# Initialize flask-migrate
migrate = Migrate(app, db)

# Use Flask Script to run DB management commands
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True
    )
)

if __name__ == "__main__":
    manager.run()
