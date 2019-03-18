#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/')
def admin_index():
    return 'admin index'
