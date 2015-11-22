#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      pyPasswordsStats.py
"""

import argparse
import os
import signal
import sys

from application import pyPasswordStats
from application.utils import python_utils
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting import condition_messages
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from domain.login import Login
from presentation.utils.clear_screen import clear_screen


if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter_version = get_interpreter_version()

    if(interpreter_version == REQUIRED_PYTHON_VERSION):

        clear_screen()

        parser = argparse.ArgumentParser(prog="pyDictStats")
        parser = argparse.ArgumentParser(description="Analyzes a " +
                                         "plain text dictionary file")
        parser.add_argument("target", help="plain text dictionary file")
        parser.add_argument("-q", "--quiet", dest="quiet",
                            action="store_true", help="quiet mode")
        parser.add_argument("-s", "--separator", dest="separator",
                            help="character that separates the accounts from "
                            "the passwords. (Default :)")
        args = parser.parse_args()

        target = args.target
        quiet_mode = args.quiet

        if(args.separator):
            separator = args.separator
        else:
            separator = ":"

        total_pass = 0
        total_types = [0, 0, 0, 0]
        passwords = {}
        lengths = {}

        if os.path.exists(target) and os.path.isfile(target):
            try:
                print("Analysing: {0}".format(target))
                print()

                f = open(target, "r", encoding="UTF-8", errors="ignore")
                total_pass = pyPasswordStats.parse_file(
                    f, total_pass, total_types, passwords, lengths, separator,
                    quiet_mode)
                f.close()

                if(total_pass > 0):
                    pyPasswordStats.print_stats(total_pass, total_types)
                    pyPasswordStats.printTop10(passwords)
                    pyPasswordStats.printMostCommonLenghts(lengths)
            except Exception as ex:
                condition_messages.print_error(ex)
        else:
            if(not os.path.exists(target)):
                condition_messages.print_error(
                    "{0} does not exists.".format(target))
                exit(1)
            if(not os.path.isfile(target)):
                condition_messages.print_error(
                    "{0} is a directory.".format(target))
                exit(1)
    else:
        condition_messages.print_error(
            'Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
