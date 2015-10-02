#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    PythonUtils.py
"""

from sys import version_info
from crosscutting import Message

def check_python_version():
    """
    Checks Python version.
    """

    required_version = 3

    if version_info < (3, 0):
        Message.print_error("Requires Python {0}".format(required_version))
        exit(1)
