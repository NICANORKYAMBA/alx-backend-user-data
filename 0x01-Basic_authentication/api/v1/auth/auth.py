#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  07 13:00:00 2023

@Author: Nicanor Kyamba
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require method

        Parameters
        ----------
        path
            Path to check
        excluded_paths
            Excluded paths

        Returns
        -------
        bool
            True if path is allowed
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Authorization header method

        Parameters
        ----------
        request
            Request object

        Returns
        -------
        str
            Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user method

        Parameters
        ----------
        request
            Request object

        Returns
        -------
        User
            User object
        """
        return None
