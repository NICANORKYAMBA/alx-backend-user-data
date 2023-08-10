#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  09 16:00:00 2023

@Author: Nicanor Kyamba
"""
from os import getenv
from flask import request, jsonify, abort
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """
    Login endpoint
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({'error': 'email missing'}), 400

    if password is None or password == '':
        return jsonify({'error': 'password missing'}), 400

    users = User.search({'email': email})
    if not users or users = []:
        return jsonify({'error': 'no user found for this email'}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            session_name = getenv('SESSION_NAME')
            response.set_cookie(session_name, session_id)
            return response
    return jsonify({'error': 'wrong password'}), 401


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def session_logout():
    """
    Logout endpoint
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
