#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  07 15:00:00 2023

@Author: Nicanor Kyamba
"""
import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decode base64 authorization header

        Args:
            base64_authorization_header (str): Base64 authorization header

        Returns:
            str: Decoded base64 authorization header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract user credentials

        Args:
            decoded_base64_authorization_header (str):
                Decoded base64 authorization header

        Returns:
            tuple: User credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user, password = decoded_base64_authorization_header.split(':', 1)

        return user, password
