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

win_pair = {
    "A": "C",
    "B": "A",
    "C": "B",
}

lose_pair = {
    "A": "B",
    "B": "C",
    "C": "A"
}


def interprate_doc():
    path = f"{os.path.join(sys.path[0], 'december/Day_2/input.txt')}"
    with open(path, 'r') as doc:
        return doc.read().splitlines()


def replace_letters():
    return [i.replace("X", "A").replace("Y", "B").replace("Z", "C") for i in interprate_doc()]


# Part 1
def rock_paper_scissors():
    win_points = 0
    pts = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    for i in replace_letters():
        opp, us = i.split(" ")
        if us == opp:
            win_points = win_points + pts[us] + 3

        elif win_pair[us] == opp:
            win_points = win_points + pts[us] + 6
        else:
            win_points += pts[us]

    print('How many win pts: ', win_points)


# Part 2
def indication_rounds():
    """
    A = lose
    B = Draw
    C = Win
    :return:
    """
    win_points = 0
    pts = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    for i in replace_letters():
        opp, indice = i.split()
        if indice == "C":
            win_points = win_points + pts[lose_pair[opp]] + 6
        elif indice == "A":
            win_points += pts[win_pair[opp]]
        else:
            win_points = win_points + pts[opp] + 3

    print("How many win pts:", win_points)
