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
    Increase the value of a key in a dictionary.
    """

    val_k = d.get(key)
    if val_k:
        d[key] = int(val_k) + 1
    else:
        d[key] = 1
