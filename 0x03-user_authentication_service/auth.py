#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  14 16:00:00 2023

@Author: Nicanor Kyamba
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password.

    :param password: The password to hash.

    :return: The hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
