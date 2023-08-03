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
    pattern = '|'.join(fields)
    return re.sub(
            rf'({pattern})=([^{separator}]*)', rf'\1={redaction}', message)


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
        super(RedactingFormatter, self).__init__(self.FORMAT)
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
        log_message = super().format(record)
        for field in self.fields:
            pattern = rf'(?<={field}=)[^{self.SEPARATOR}\
                    ]*(?={self.SEPARATOR})|(?<={field}=)[^{self.SEPARATOR}]*$'
            log_message = re.sub(pattern, self.REDACTION, log_message)
        return log_message
