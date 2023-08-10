#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Aug  10 14:00:00 2023

@Author: Nicanor Kyamba
"""
from models.base import Base


class UserSession(Base):
    """
    UserSession model
    """
    def __init__(self, *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
