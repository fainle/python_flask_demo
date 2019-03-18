#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<user_name>')
def profile(user_name):
    return '{} profile'.format(user_name)


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login', next='/login'))
    print(url_for('profile', user_name='aa'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)