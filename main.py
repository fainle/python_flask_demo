#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask('a')


@app.route('/')
def main():
    return 'hello world!'
