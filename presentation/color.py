#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      color.py
"""


class Color:
    """
    Class color
        Colors the text to display it in the output.
    """

    bold = "\033[1m"

    green = "\033[32m"
    red = "\033[31m"
    yellow = "\033[33m"

    bold_green = "{0}{1}".format(bold, green)
    bold_red = "{0}{1}".format(bold, red)
    bold_yellow = "{0}{1}".format(bold, yellow)

    end = "\033[0m"
