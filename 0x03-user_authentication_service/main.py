#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  15 21:30:00 2023

@Author: Nicanor Kyamba
"""
import requests


BASE_URL = 'http://127.0.0.1:5000'


def register_user(email: str, password: str) -> None:
    """
    Register a new user
    """
    url = f'{BASE_URL}/users'
    payload = {
            'email': email,
            'password': password
            }
    response = requests.post(url, json=payload)
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Test login functionality
    """
    url = f'{BASE_URL}/login'
    payload = {
            'email': email,
            'password': password
            }
    response = requests.post(url, json=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Test login success
    """
    url = f'{BASE_URL}/login'
    payload = {
            'email': email,
            'password': password
            }
    response = requests.post(url, json=payload)
    assert response.status_code == 200


def profile_unlogged() -> None:
    """
    Test user profile retrieval
    """
    url = f'{BASE_URL}/profile'

    response = requests.get(url)

    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Test user profile retrieval
    """
    url = f'{BASE_URL}/profile'

    payload = {
            'session_id': session_id
            }

    response = requests.get(url, payload)

    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """
    Test logout user functionality
    """
    url = f'{BASE_URL}/sessions'

    payload = {
            'session_id': session_id
            }

    response = requests.delete(url, payload)

    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """
    Test reset password functionality
    """
    url = f'{BASE_URL}/reset_password'

    payload = {
            'email': email
            }

    response = requests.post(url, payload)

    assert response.status_code == 200


def update_password(email: str,
                    reset_token: str,
                    new_password: str) -> None:
    """
    Test the update password functionality
    """
    url = f'{BASE_URL}/reset_password'

    payload = {
            'email': email,
            'reset_token': reset_token,
            'new_password': new_password
            }

    response = requests.put(url, payload)

    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
