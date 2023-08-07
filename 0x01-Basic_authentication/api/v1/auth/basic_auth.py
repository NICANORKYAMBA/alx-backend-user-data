#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  07 15:00:00 2023

@Author: Nicanor Kyamba
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extract base64 authorization header

        Args:
            authorization_header (str): Authorization header

        Returns:
            str: Base64 authorization header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]
