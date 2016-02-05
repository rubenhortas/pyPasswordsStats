#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      login.py
"""

from domain.security_level import SecurityLevel
from presentation.tag import Tag


class Login:

    account = None
    password = None
    password_security = None

    def __init__(self, account, password):
        self.account = account
        self.password = password

        self.password_security = SecurityLevel.strong

        if self.password:
            if len(self.password) <= 14:
                self.password_security = SecurityLevel.medium

                if len(self.password) <= 8:
                    self.password_security = SecurityLevel.weak

                    if self.password in self.account:
                        self.password_security = SecurityLevel.very_weak

                    elif self.password.isdigit():  # password is only numeric
                        self.password_security = SecurityLevel.very_weak

                    # password is only alphabetic
                    elif self.password.isalpha():
                        self.password_security = SecurityLevel.very_weak
        else:
            self.password_security = SecurityLevel.blank

    def print_info(self):
        """
        print_info(self)
            Prints info about password strength.
        """

        if self.password_security == SecurityLevel.strong:
            tag = Tag.strong
        elif self.password_security == SecurityLevel.medium:
            tag = Tag.medium
        elif self.password_security == SecurityLevel.weak:
            tag = Tag.weak
        elif self.password_security == SecurityLevel.very_weak:
            tag = Tag.very_weak
        else:
            tag = Tag.blank

        print(("{0} {1}/{2}").format(tag, self.account, self.password))
