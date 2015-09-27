#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    PythonUtils.py
"""

import sys
from crosscutting import Message

def check_python_version():
    """
    Checks Python version.
    """

    required_version = 3

    major, minor, micro, releaselevel, serial = sys.version_info
    if (major, minor) < (required_version, 0):
        Message.print_error("Requires Python {0}".format(required_version))
        exit(1)
