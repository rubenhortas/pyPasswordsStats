#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      Message.py
"""

from presentation.Tag import Tag

def print_error(err_msg):
    print("{0} {1}".format(Tag.error, err_msg))


def info_msg(msg):
    """
    info_msg(msg)
        Prints an information message.
    Arguments:
        - msg: (string) Information message.
    """

    print("{0} {1}".format(Tag.info, msg))
