"""Advent of Code 2023 - Day 1
Date: 01/12/2023
Author: @Shubhamm33 (github) 
"""

import os
from logger import logger

# utils---
def remove_new_line_character(val:str):
    newline_character = str(val).endswith("\n")
    if newline_character:
        val = str(val).removesuffix("\n")
        return val
    else:
        return val

def get_first_last_digit(val:str):

    digits = []
    for each_val in val:
        if each_val.isdigit():
            digits.append(each_val)
    # logger.info(digits)

    if len(digits) == 0:
        return None
    
    elif len(digits) == 1:
        num = digits[0] + digits[0]
        num = int(num)
        return num
    
    elif len(digits) > 1:
        num = digits[0] + digits[-1]
        num = int(num)
        return num
    
    return digits

def evaluate_str(val):
    # logger.info(val)

    digits = []

    string_representation = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
        'zero': 'z0o',
    }

    for key, value in string_representation.items():
        if key in val:
            val = str(val).replace(key, value)
    
    for each_val in val:
        if each_val.isdigit():
            digits.append(each_val)
            
    if len(digits) == 0:
        return None
    
    elif len(digits) == 1:
        num = digits[0] + digits[0]
        num = int(num)
        return num
    
    elif len(digits) > 1:
        num = digits[0] + digits[-1]
        num = int(num)
        return num
    
    return digits

# ---


def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day1.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    digits = list(map(get_first_last_digit, lines))
    # logger.info(digits)

    final_sum_of_calibration = sum(digits)
    logger.info(f"Final sum of calibration Q1: {final_sum_of_calibration}")

def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day1.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    digits = list(map(evaluate_str, lines))
    final_sum_of_calibration = sum(digits)
    # logger.info(digits)
    logger.info(f"Final sum of calibration Q2: {final_sum_of_calibration}")



if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()