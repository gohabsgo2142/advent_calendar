# coding: utf-8
"""
---------------------------
File : day_6.py
Create by : jarvis
Puzzle date : 2022-12-06
---------------------------
"""

import os
import sys


def interprate_doc():
    path = f"{os.path.join(sys.path[0], 'december/Day_6/input.txt')}"
    with open(path, 'r') as doc:
        return doc.read().splitlines()


def reading_lines():
    """"""
    print(interprate_doc())
