#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      Login.py
"""
from Tag import Tag

class Login:

    account = None
    pwd = None
    psec = None # 0 is very weak; 1 is weak; 2 is medium
                # 3 is strong

    def __init__(self, account, password):
        self.account  = account
        self.pwd = password

        # Get password type (very weak/weak/medium/strong)
        # default password sec = 3 (strong)
        self.psec = 3
        if len(self.pwd) <= 14:
            self.psec = 2 # medium
            if len(self.pwd) <= 8:
                self.psec = 1 # weak

                # Detect Very Weak Passwords
                # password is in account
                if self.pwd in self.account:
                    self.psec = 0 # very weak
                # password is only numeric
                elif self.pwd.isdigit():
                    self.psec = 0
                #p password is only alphabetic
                elif self.pwd.isalpha():
                    self.psec = 0

    def Print_info(self):
        """
        Print info about password strength
        """

        if self.psec == 3:
            tag = Tag.strong
        elif self.psec == 2:
            tag = Tag.medium
        elif self.psec == 1:
            tag = Tag.weak
        else:
            tag = Tag.very_weak

        print(("{0} {1}/{2}").format(tag, self.account, self.pwd))