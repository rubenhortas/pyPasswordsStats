#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        dictionary_utils.py
@interpreter: python3
"""


def increase_key_value(d, key):
    """
    increase_key_value(d, key)
        Increases the value of a key in a dictionary.
    Arguments:
        d: (dictionary) Dictionary.
        key: Key.
    """

    if d.get(key):
        d[key] = int(key) + 1
    else:
        d[key] = 1
