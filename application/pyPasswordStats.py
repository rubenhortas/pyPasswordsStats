#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        pyPasswordStats.py
@interpreter: python3
"""

from crosscutting.condition_messages import print_error
from domain.login import Login


def parse_file(f, separator, quiet_mode, sumary):
    """
    parse_file(f, separator, quiet_mode, sumary):
        Parses a login-password file
    Arguments:

        f: (file) Login-password file.
        separator: (char) Character delimiter for login-password.
        quiet_mode: (boolean) Indicates if the program is running on quiet mode.
        sumary: (sumarty) Stores the results.
    """

    for line in f:
        info = line.split(separator)

        if len(info) == 2:
            sumary.inc_logins()

            account = info[0].strip().lower()
            password = info[1].strip()
            login = Login(account, password)

            if not quiet_mode:
                login.print_info()

            login_security = login.password_security

            sumary.inc_types_usage(login_security)
            sumary.inc_password_usage(login.password)

            if password != "":
                password_length = len(login.password)
                sumary.inc_lenght_usage(password_length)

        else:
            print_error("{0} Wrong line format.".format(line.strip()))
