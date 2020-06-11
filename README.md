# Project Trending

### This is a site where you can see what is trending globally or near you on Twitter.

I'm using Flask as a backend and Angular frontend for this project.

### To get started ...

Clone this project and and the frontend https://github.com/XzavierDunn/Project-Trending-Angular. After that you have to install the angular cli and run npm install in the project directory for the frontend. After that stops you can run the app with ng serve -o.

To run the backend just setup these environment variables then start a virtual environment with `python3 -m venv venv` enter it `. venv/bin/activate` on macOS or linux then `pip install -r requirements.txt`.

No database required you only need to create an app through https://developer.twitter.com/en/apps and then use all four tokens as environment variables.
Linux/MacOS:

```
export consumer_key='API Key'
export consumer_secret='API secret key'
export access_token='Access token'
export access_token_secret='Access token secret'

python app.py
```

Tweepy - http://docs.tweepy.org
Tweepy Github - https://github.com/tweepy/tweepy

- Xzavier Dunn
