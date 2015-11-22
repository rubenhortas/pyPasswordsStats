#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@status:    Developing
@version:   alpha
@file:      tag.py
"""

from .color import Color


class Tag:
    """
    Defines the tags for each message shown in the output.
    """

    info = "[" + Color.green + "*" + Color.end + "]"
    error = "{0}{1}!{2}{3}".format("[", Color.bold_red, Color.end, "]")

    strong = "{0}{1}strong{2}{3} ".format("[", Color.green, Color.end, "]")
    medium = "{0}{1}medium{2}{3} ".format("[", Color.yellow, Color.end, "]")
    weak = "{0}{1}  weak{2}{3} ".format("[", Color.red, Color.end, "]")
    very_weak = "{0}{1}v weak{2}{3} ".format(
        "[", Color.bold_red, Color.end, "]")
