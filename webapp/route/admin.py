#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/')
def admin_index():
    return 'admin index'


@admin_bp.route('/admin/login', methods=['get', 'post'])
def admin_login():
    if request.method == 'post':
        username = request.form['username']
        password = request.form['password']

        # todo check pass
        pass

    return render_template('admin/login.html')
