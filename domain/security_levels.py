#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        security_levels.py
@interpreter: python3
"""

from enum import Enum


class SecurityLevel:
    blank = 0
    very_weak = 1
    weak = 2
    medium = 3
    strong = 4
