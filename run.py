import os

from dotenv import load_dotenv

from app import createApp


env_path = os.path.join('.', '.env')
load_dotenv(dotenv_path=env_path)

app = createApp()
app.config.from_object(os.environ['APP_SETTINGS'])

if __name__ == 'main':
    app.run()