#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
from flask import url_for, redirect, session


def login_required(view):
    @functools.wraps(view)
    def _(**kwargs):
        if session.get('admin_name') is None:
            return redirect(url_for('admin_bp.admin_login'))

        return view(**kwargs)
    return _
