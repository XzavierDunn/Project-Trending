
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db

env_name = os.getenv('FLASK_ENV')
application = create_app(env_name)

migrate = Migrate(app=application, db=db)

manager = Manager(app=application)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
