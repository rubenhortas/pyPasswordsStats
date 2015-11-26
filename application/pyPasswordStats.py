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

import collections

from crosscutting import condition_messages
from domain.login import Login
from domain.security_levels import SecurityLevel

from .utils import dictionary_utils


def parse_file(f, num_logins, types_usage, passwords_usage, lengths_usage,
               separator, quiet_mode):
    """
    parse_file(f, num_logins, types_usage, passwords_usage, lengths_usage,
               separator, quiet_mode):
        Parses a login-password file
    Arguments:
        - f: (file) Login-password file.
        - num_logins: (int) Total number of logins.
        - types_usage: (array) Counter for types usage.
        - passwords_usage: (dictionary) Dictionary for passwords usage.
        - legths_usage: (dictionary) Dictionary for lengths usage.
        - separator: (char) Character delimiter for login-password.
        - quiet_mode: (boolean) Indicates if the program is running on quiet mode.
    """

    for line in f:
        info = line.split(separator)

        if len(info) == 2:
            num_logins = num_logins + 1

            account = info[0].strip().lower()
            password = info[1].strip()

            if password != "":
                login = Login(account, password)
                if not quiet_mode:
                    login.print_info()

                login_security = login.password_security

                types_usage[login_security] = types_usage[login_security] + 1

                dictionary_utils.increase_key_value(
                    passwords_usage, login.password)

                length_password = len(login.password)
                dictionary_utils.increase_key_value(
                    lengths_usage, length_password)

            else:
                types_usage[0] = types_usage[SecurityLevel.very_weak] + 1
                dictionary_utils.increase_key_value(lengths_usage, 0)
        else:
            Message.print_error("{0} Wrong line format.".format(line.strip()))

    return num_logins


def print_usage_stats(total, total_types):
    """
    print_usage_stats(total)
        Prints the results of the statistical analysis.
    Arguments:
        - total: (int) total of parsed lines.
    """

    very_weak = total_types[SecurityLevel.very_weak]
    weak = total_types[SecurityLevel.weak]
    medium = total_types[SecurityLevel.medium]
    blank = total_types[SecurityLevel.strong]

    if total > 0:
        blank_percent = (blank * 100) / total
        vweak_percent = (very_weak * 100) / total
        weak_percent = (weak * 100) / total
        medium_percent = (medium * 100) / total

    print()
    condition_messages.print_info(
        "SUMMARY ----------------------------------------------------")
    print()
    condition_messages.print_info("Total passwords: {0}".format(total))
    print()
    if total > 0:
        condition_messages.print_info("Blank passwords: {0} ({1:0.2f}%)".format(blank,
                                                                                blank_percent))
        condition_messages.print_info("Very weak passwords: {0} ({1:0.2f}%)".format(very_weak,
                                                                                    vweak_percent))
        condition_messages.print_info(
            "Weak passwords: {0} ({1:0.2f}%)".format(weak, weak_percent))
        condition_messages.print_info("Medium passwords: {0} ({1:0.2f}%)".format(medium,
                                                                                 medium_percent))
    print()


def print_top10(passwords):
    """
    print_top_10(passwords)
        Displays Top 10 most used passwords.

    Arguments:
        - passwords: (dictionary) Password dictionary.
    """

    if len(passwords) > 0:
        i = 1
        condition_messages.print_info("Top 10 used passwords:")
        top10 = collections.Counter(passwords).most_common(10)
        for pair in top10:
            condition_messages.print_info(
                "\t{0}) {1} ({2} times)".format(i, pair[0], pair[1]))
            i = i + 1


def print_most_common_lengths(lengths):
    """
    printMostCommonLen(lengths)
        Displays most common lengths usage.
    Arguments:
        - lengths: (dictionary) Lengths dictionary.
    """

    if len(lengths) > 0:
        most_length_usage = collections.Counter(lengths).most_common(1)[0]
        print()
        condition_messages.print_info("Most length usage: {0} chars ({1} times)".format(most_length_usage[0],
                                                                                        most_length_usage[1]))
