# coding: utf-8
"""
---------------------------
File : day_3.py
Create by : jarvis
Puzzle date : 2022-12-03
---------------------------
"""

import itertools
import os
import sys

path = f"{os.path.join(sys.path[0], 'input.txt')}"


def read_document():
    count = 0
    with open(path, 'r') as doc:
        for i in doc:
            sentence = i.strip('\n')
            n = len(sentence)
            if n % 2 == 0:
                f_half = sentence[:n // 2]
                s_half = sentence[n // 2:]
            else:
                f_half = sentence[:n // 2 + 1]
                s_half = sentence[n // 2 + 1:]
            for x in find_duplicate(f_half, s_half):
                count = get_letter_number(x) + count
    return count


def compare_lines():
    full_doc, count = [], 0
    with open(path, 'r') as doc:
        full_doc.extend(e.strip('\n') for e in doc)
        for i in range(0, len(full_doc), 3):
            x = set(find_duplicate(full_doc[i], full_doc[i + 1]))
            y = set(find_duplicate(full_doc[i], full_doc[i + 2]))
            z = set(find_duplicate(full_doc[i + 1], full_doc[i + 2]))
            same_inter = list(x.intersection(y, z))[0]
            count = get_letter_number(same_inter) + count

    return count


def get_letter_number(letter):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38


def find_duplicate(f_half, s_half):
    return (j for j, k in itertools.product(set(f_half), set(s_half)) if j == k)
