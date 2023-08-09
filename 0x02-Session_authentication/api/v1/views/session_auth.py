#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  09 16:00:00 2023

@Author: Nicanor Kyamba
"""
from os import getenv
from flask import request, jsonify
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

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404

    if not users or users = []:
        return jsonify({'error': 'no user found for this email'}), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({'errror': 'wrong password'}), 401

    from api.v1.app import auth

    user = users[0]
    session_id = auth.create_session(user.id)

    SESSION_NAME = getenv('SESSION_NAME')
    user_json = user.to_json()

    response = jsonify(user_json)
    response.set_cookie(SESSION_NAME, session_id)

    return response
