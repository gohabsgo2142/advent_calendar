# coding: utf-8
"""
---------------------------
File : day_1.py
Create by : jarvis
Puzzle date : 2022-12-01
---------------------------
"""
import os
import sys


def read_document():
    first_part, second_part = []
    path = f"{os.path.join(sys.path[0], 'input.txt')}"
    with open(path, 'r') as doc:
        for i in doc:
            sentence = i.strip('\n')
            n = len(sentence)
            if n % 2 == 0:
                f_half = sentence[:n // 2]
                s_half = sentence[n // 2:]
            else:
                f_half = sentence[:n // 2+1]
                s_half = sentence[n // 2+1:]
            


if __name__ == '__main__':
    read_document()
