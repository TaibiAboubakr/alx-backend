#!/usr/bin/env python3
""" app """


from flask import Flask
from flask_babel import Babel
from flask import render_template
app = Flask(__name__)
babel = Babel(app)


class Config():
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def home():
    """ home page """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
