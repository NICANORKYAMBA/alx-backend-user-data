#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  03 15:00:00 2023

@Author: Nicanor Kyamba
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt

    Parameters
    ----------
    password : str
        The password to be hashed

    Returns
    -------
    bytes
        The salted, hashed password as a byte string
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
