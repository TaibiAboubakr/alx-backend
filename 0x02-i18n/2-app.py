#!/usr/bin/env python3
""" app """


from flask import Flask
from flask_babel import Babel
from flask import render_template
from flask import g, request


class Config(object):
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)



@babel.localeselector
def get_locale():
    """if a user is logged in, use the locale from the user settings"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['en','fr'])


@app.route('/')
def home():
    """ home page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
