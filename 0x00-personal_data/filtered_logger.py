#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Aug  03 12:00:00 2023

@Author: Nicanor Kyamba
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
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
    for field in fields:
        message = re.sub(
            rf'({field})=([^{separator}]*)', rf'\1={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Constructor

        Parameters
        ----------
        fields : list
            List of fields to filter

        Returns
        -------
        None
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats a record

        Parameters
        ----------
        record : logging.LogRecord
            Record to format

        Returns
        -------
        str
            Formatted record
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super().format(record)
