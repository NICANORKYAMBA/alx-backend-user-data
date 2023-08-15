#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  15 09:00:00 2023

@Author: Nicanor Kyamba
"""
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, jsonify, request, abort


app = Flask(__name__)


AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Returns the index page
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    Route to register a new user
    """
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = AUTH.register_user(email, password)

        return jsonify({"email": "{}".format(user.email),
                        "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    Route to login a user
    """
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        validate_login = AUTH.valid_login(email, password)

        if validate_login:
            session_id = AUTH.create_session(email)
            response_data = {
                    "email": email,
                    "message": "logged in"
                    }
            response = jsonify(response_data)

            response.set_cookie('session_id', value=session_id)

            return response, 200
        else:
            abort(401)
    except NoResultFound:
        abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000")
