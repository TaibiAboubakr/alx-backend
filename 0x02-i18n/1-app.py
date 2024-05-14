#!/usr/bin/env python3
""" app """


from flask import Flask
from flask_babel import Babel
from flask import render_template


class Config():
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def home():
    """ home page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
