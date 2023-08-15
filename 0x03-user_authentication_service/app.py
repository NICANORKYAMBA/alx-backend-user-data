#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  15 09:00:00 2023

@Author: Nicanor Kyamba
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Returns the index page
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000")
