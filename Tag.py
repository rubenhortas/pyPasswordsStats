#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@status:    Developing
@version:   alpha
@file:      Tag.py
"""

from Color import Color


class Tag:
    """
    Defines the tags for each message shown in the output.
    """

    strong = '[' + Color.green + 'strong' + Color.end + '] '
    medium = '[' + Color.yellow + 'medium' + Color.end + '] '
    weak = '[' + Color.red + ' weak ' + Color.end + '] '
    very_weak = '[' + Color.bold_red + 'v weak' + Color.end + '] '
        
        
#     error = "[" + Color.bold_red + "ERROR" + Color.end + "]"
#     info = "[" + Color.green + "*" + Color.end + "] "
#     warning = "[" + Color.bold_yellow + "WARNING" + Color.end + "]"
#     move = Color.bold_yellow + "->" + Color.end
#     debug = ">>"
#     ex = "[" + Color.bold_red + "EXCEPTION!]:"
