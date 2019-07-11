import os 

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)
    app.run(host='0.0.0.0')
