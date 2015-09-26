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
import collections
import os
import sys

import crosscutting.Message as Message
from domain.Login import Login


def __parse_file(f, total_logins, type_array, pwd_dict, len_dict):
    for line in f:
        info = line.split(separator)

        if(len(info) == 2):
            total_logins = total_logins + 1

            account = info[0].strip().lower()
            password = info[1].strip()

            if(password != ""):
                login = Login(account, password)
                if not quiet_mode:
                    login.Print_info()

                # Inc Counters
                sec = login.psec
                if sec < 3:  # not an strong password
                    type_array[sec] = type_array[sec] + 1

                # Password usage
                __inc_dict(pwd_dict, login.pwd)

                # Length usage
                len_pwd = len(login.pwd)
                __inc_dict(len_dict, len_pwd)

            else:
                type_array[3] = type_array[3] + 1
                __inc_dict(len_dict, 0)
        else:
            Message.print_error("{0} Wrong line format.".format(line.strip()))

    return total_logins

def __inc_dict(d, key):
    """
    Increase the value of a key in a dictionary.
    """

    val_k = d.get(key)
    if val_k:
        d[key] = int(val_k) + 1
    else:
        d[key] = 1

def __print_stats(total):
    """
    TODO: Comment this.
    """

    very_weak = type_array[0]
    weak = type_array[1]
    medium = type_array[2]
    blank = type_array[3]

    if total > 0:
        blank_percent = (blank * 100) / total
        vweak_percent = (very_weak * 100) / total
        weak_percent = (weak * 100) / total
        medium_percent = (medium * 100) / total

    print()
    print("SUMMARY ----------------------------------------------------")
    print()
    print ("Total passwords: {0}".format(total))
    print()
    if(total > 0):
        print("Blank passwords: {0} ({1:0.2f}%)".format(blank, blank_percent))
        print("Very weak passwords: {0} ({1:0.2f}%)".format(very_weak,
                                                    vweak_percent))
        print("Weak passwords: {0} ({1:0.2f}%)".format(weak, weak_percent))
        print("Medium passwords: {0} ({1:0.2f}%)".format(medium,
                                                         medium_percent))
        print()
        __printTop10()
        print()
        __printMostCommonLen()
    print()
    print("------------------------------------------------------------")

def __printTop10():
    """
    Displays Top 10 most used passwords.
    """

    if(len(pwd_dict) > 0):
        i = 1
        print("Top 10 used passwords:")
        l_top10 = collections.Counter(pwd_dict).most_common(10)
        for pair in l_top10:
            print("\t{0}) {1} ({2} times)".format(i, pair[0], pair[1]))
            i = i + 1


def __printMostCommonLen():
    """
    Displays most common length usage.
    """

    if(len(len_dict) > 0):
        # collections.Counter().most_common() returns a list of tuples
        # in this case, the list only has an item (a tuple), get it
        mclu_tuple = collections.Counter(len_dict).most_common(1)[0]
        # display the tuple in a format pleasing to the eye
        print("Most length usage: {0} chars ({1} times)".format(mclu_tuple[0],
                                                              mclu_tuple[1]))

def __check_python_version():
    """
    Checks Python version.
    """

    major, minor, micro, releaselevel, serial = sys.version_info
    if (major, minor) < (3, 0):
        Message.print_error("Requires Python 3")
        exit(1)

if __name__ == "__main__":

    # Parse input arguments
    parser = argparse.ArgumentParser(prog="pyDictStats")
    parser = argparse.ArgumentParser(description="Analyzes a " +
                                     "plain text dictionary file")
    parser.add_argument("target", help="plain text dictionary file")
    parser.add_argument("-q", "--quiet", dest="quiet",
                        action="store_true", help="quiet mode")
    parser.add_argument("-s", "--separator", dest="separator",
                        help="character that separates the accounts from " \
                        "the passwords. (Default :)")
    args = parser.parse_args()

    target = args.target
    quiet_mode = args.quiet

    if(args.separator):
        separator = args.separator
    else:
        separator = ":"

    __check_python_version()

    # Array for store the count of passwords types
    # [Very_weak (pos 0), Weak (pos 1), Medium (pos 2), Blank (pos 3)
    total_pass = 0
    type_array = [0, 0, 0, 0]
    pwd_dict = {}
    len_dict = {}

    # TODO: FIX THIS: Add an else
    if os.path.exists(target) and os.path.isfile(target):
        f = open(target, "r", encoding="utf-8", errors="ignore")
        print("Analysing: {0}".format(target))
        total_pass = __parse_file(f, total_pass, type_array, pwd_dict, len_dict)
        f.close()

        __print_stats(total_pass)
    else:
        if(not os.path.exists(target)):
            Message.print_error("{0} does not exists.".format(target))
            exit(1)
        if(not os.path.isfile(target)):
            Message.print_error("{0} is a directory.".format(target))
            exit(1)
