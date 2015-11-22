#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      condition_messages.py
"""

from presentation.tag import Tag


def print_error(err_msg):
    print("{0} {1}".format(Tag.error, err_msg))


def print_info(msg):
    """
    print_info(msg)
        Prints an information message.
    Arguments:
        - msg: (string) Information message.
    """

    print("{0} {1}".format(Tag.info, msg))
