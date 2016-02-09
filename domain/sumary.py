#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      sumary.py
"""
import collections

from application.utils import dictionary_utils
from crosscutting.condition_messages import print_info
from domain.security_level import SecurityLevel


class Sumary:
    num_logins = None
    types_usage = None
    passwords_usage = None
    lengths_usage = None

    def __init__(self):
        self.num_logins = 0
        self.types_usage = [0, 0, 0, 0, 0]
        self.passwords_usage = {}
        self.lengths_usage = {}

    def inc_logins(self):
        self.num_logins = self.num_logins + 1

    def inc_types_usage(self, login_security):
        self.types_usage[login_security] = self.types_usage[login_security] + 1

    def inc_password_usage(self, password):
        dictionary_utils.increase_key_value(self.passwords_usage, password)

    def inc_lenght_usage(self, password_length):
        dictionary_utils.increase_key_value(self.lengths_usage, password_length)

    def print_stats(self):
        if self.num_logins > 0:
            print()
            print_info("SUMMARY ----------------------------------------------------")
            print()
            print_info("Total logins: {0}".format(self.num_logins))
            print()
            self.print_usage_stats(self.num_logins, self.types_usage)
            self.print_top10(self.passwords_usage)
            self.print_most_common_lengths(self.lengths_usage)

    @staticmethod
    def print_usage_stats(total, total_types):
        """
        print_usage_stats(total)
            Prints the results of the statistical analysis.
        Arguments:
            total: (int) total of parsed lines.
            total_types: (int) total of types.
        """

        very_weak = total_types[SecurityLevel.very_weak]
        weak = total_types[SecurityLevel.weak]
        medium = total_types[SecurityLevel.medium]
        blank = total_types[SecurityLevel.blank]

        blank_percent = (blank * 100) / total
        vweak_percent = (very_weak * 100) / total
        weak_percent = (weak * 100) / total
        medium_percent = (medium * 100) / total

        print_info("Blank passwords: {0} ({1:0.2f}%)".format(blank, blank_percent))
        print_info("Very weak passwords: {0} ({1:0.2f}%)".format(very_weak, vweak_percent))
        print_info("Weak passwords: {0} ({1:0.2f}%)".format(weak, weak_percent))
        print_info("Medium passwords: {0} ({1:0.2f}%)".format(medium, medium_percent))
        print()

    # noinspection PyArgumentList
    def print_top10(self, passwords):
        """
        print_top_10(passwords)
            Displays Top 10 most used passwords.

        Arguments:
            passwords: (dictionary) Password dictionary.
        """

        if len(passwords) > 0:
            i = 1
            print_info("Top 10 used passwords:")
            top10 = collections.Counter(self.passwords_usage).most_common(10)
            for pair in top10:
                print_info("\t{0}) {1} ({2} times)".format(i, pair[0], pair[1]))
                i = i + 1

    # noinspection PyArgumentList
    def print_most_common_lengths(self, lengths):
        """
        printMostCommonLen(lengths)
            Displays most common lengths usage.
        Arguments:
            lengths: (dictionary) Lengths dictionary.
        """

        if len(lengths) > 0:
            most_length_usage = collections.Counter(self.lengths_usage).most_common(1)[0]
            print()
            print_info("Most length usage: {0} chars ({1} times)".format(most_length_usage[0], most_length_usage[1]))
