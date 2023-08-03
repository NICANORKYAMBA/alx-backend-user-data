#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Aug  03 12:00:00 2023

@Author: Nicanor Kyamba
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Function to filter a message based on a list of fields

    Parameters
    ----------
    fields : list
        List of fields to filter
    redaction : str
        String to replace fields
    message : str
        String to filter
    separator : str
        String to separate fields

    Returns
    -------
    str
        Filtered message
    """
    pattern = '|'.join(fields)
    return re.sub(
            rf'({pattern})=([^{separator}]*)', rf'\1={redaction}', message)
