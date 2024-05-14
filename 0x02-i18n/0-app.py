#!/usr/bin/env python3
""" app """


from flask import Flask
from flask import render_template
app = Flask(__name__)


app.route('/')


def home():
    """ home page """
    return render_template('0-index.html')
