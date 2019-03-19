#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, session, redirect, url_for

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/')
def admin_index():

    next = request.args.get('next', 'welcome')
    return render_template('layout/base_iframe.html', next=next)


@admin_bp.route('/admin/login', methods=['get', 'post'])
def admin_login():
    if request.method == 'post':
        username = request.form['username']
        password = request.form['password']
        error = None

        data = dict()

        if error is None:
            session.clear()
            session['admin_name'] = username
            data['status_code'] = 1
            data['url'] = url_for('admin_bp.admin_index')
        else:
            data['status_code'] = 0
            data['msg'] = error

    return render_template('admin/login.html')


@admin_bp.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_bp.admin_index'))
