#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  14 16:00:00 2023

@Author: Nicanor Kyamba
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hash a password.

    :param password: The password to hash.

    :return: The hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Constructor.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user.

        Args:
            email: The email of the user.
            password: The password of the user.

        Returns:
            The user object.
        """
        if email is None or password is None:
            return None

        try:
            existing_user = self._db.find_user_by(email=email)

            if existing_user:
                raise ValueError("User {} already exists.".format(email))

            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        except Exception as e:
            return None
