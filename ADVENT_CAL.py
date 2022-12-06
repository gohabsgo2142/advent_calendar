# coding: utf-8
"""
---------------------------
File : ADVENT_CAL.py
Create by : jarvis
Puzzle date : 2022-12-01
---------------------------
"""

import argparse
from december.Day_1 import day_1 as d1
from december.Day_2 import day_2 as d2
from december.Day_3 import day_3 as d3
from december.Day_4 import day_4 as d4
from december.Day_5 import day_5 as d5
from december.Day_6 import day_6 as d6


def get_args() -> argparse.Namespace:
    """Define the argpas command line args."""
    parser = argparse.ArgumentParser(description="Advent calendar project")
    parser.add_argument('-d', '--dates', type=int, help='Add the report to QA_DB')
    return parser.parse_args()


if get_args() is not None:
    """Start the logic"""

if get_args().dates == 1:
    d1.elf_calculation()

if get_args().dates == 2:
    d2.rock_paper_scissors()
    d2.indication_rounds()

if get_args().dates == 3:
    d3.read_document()
    d3.compare_lines()

# if get_args().dates == 4:
#     d4.
#     d4.

# if get_args().dates == 5:
#     d5.
#     d5.

if get_args().dates == 6:
    d6.reading_lines()
