#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  09 14:00:00 2023

@Author: Nicanor Kyamba
"""
import uuid
from typing import Dict
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Class SessionAuth"""

    user_id_by_session_id: Dict[str, str] = {}

    def create_session(
            self, user_id: str = None) -> str:
        """
        Method to create a session

        Args:
            user_id (str, optional): user id. Defaults to None.

        Returns:
            str: session id
        """
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(
            self, session_id: str = None) -> str:
        """
        Method that returns the user id for a given session id

        Args:
            session_id (str, optional): session id. Defaults to None.

        Returns:
            str: user id
        """
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
