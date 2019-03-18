#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/')
def admin_index():
    return 'admin index'


@admin_bp.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')
