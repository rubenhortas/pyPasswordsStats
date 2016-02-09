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

from application.pyPasswordStats import parse_file
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.condition_messages import print_info
from crosscutting.constants import DEFAULT_SEPARATOR
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from domain.sumary import Sumary
from presentation.utils.screen import clear_screen

if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter_version = get_interpreter_version()

    if interpreter_version == REQUIRED_PYTHON_VERSION:

        clear_screen()

        parser = argparse.ArgumentParser(prog="pyDictStats")
        parser = argparse.ArgumentParser(description="Analyzes a plain text dictionary file for statistical analysis")
        parser.add_argument("target", help="plain text dictionary file")
        parser.add_argument("-q", "--quiet", dest="quiet", action="store_true", help="quiet mode")
        parser.add_argument("-s", "--separator", dest="separator",
                            help="character that separates the accounts from the passwords_usage. (Default ':')")
        args = parser.parse_args()

        target = args.target
        quiet_mode = args.quiet

        if args.separator:
            separator = args.separator
        else:
            separator = DEFAULT_SEPARATOR

        print_info("Analyzing: {0}\n".format(target))

        if os.path.exists(target) and os.path.isfile(target):
            try:
                sumary = Sumary()
                f = open(target, "r", encoding="UTF-8", errors="ignore")
                parse_file(f, separator, quiet_mode, sumary)
                f.close()
                sumary.print_stats()
            except Exception as ex:
                print_error(ex)
        else:
            if not os.path.exists(target):
                print_error("{0} does not exists.".format(target))
            if not os.path.isfile(target):
                print_error("{0} is a directory.".format(target))
            exit(1)
    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
