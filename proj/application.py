import os 

from src.app import create_app

env_name = os.getenv('FLASK_ENV')
application = create_app(env_name)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
