import os, math
from logger import logger
import time

# utils---
def remove_new_line_character(val:str):
    newline_character = str(val).endswith("\n")
    if newline_character:
        val = str(val).removesuffix("\n")
        return val
    else:
        return val

def convert_to_int_list(val):
    val = val.split(" ")
    val = list(map(int, val))
    val.reverse()
    return val

def subtract_left_to_right(val:list):
    try:
        steps = []
        steps.append(val)
        arr = val
        while not any(arr) == 0:
            substitute = []
            for i in range(len(arr)):
                if i+1 < len(arr):
                    substitute.append(arr[i] - arr[i+1])

            arr = substitute
            steps.append(arr)

    except:
        logger.error('ERR', exc_info=True)

    steps.reverse()
    steps[0].append(0)

    for i in range(len(steps)):
        if i+1 < len(steps):
            steps[i+1].insert(0, steps[i][0] + steps[i+1][0])
    
    return steps[-1][0]


def subtract_part_2(val:list):
    try:
        steps = []
        steps.append(val)
        arr = val
        while not any(arr) == 0:
            substitute = []
            for i in range(len(arr)):
                if i+1 < len(arr):
                    substitute.append(arr[i] - arr[i+1])

            arr = substitute
            steps.append(arr)

    except:
        logger.error('ERR', exc_info=True)

    steps.reverse()
    steps[0].append(0)
    steps = list(map(lambda x: x[::-1], steps))

    for i in range(len(steps)):
        if i+1 < len(steps):
            steps[i+1].insert(0, steps[i+1][0] - steps[i][0])

    return steps[-1][0]

def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day9.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()

    lines = list(map(remove_new_line_character, lines))
    lines = list(map(convert_to_int_list, lines))

    lines = list(map(subtract_left_to_right, lines))
    logger.info(f"Sum of these extrapolated values Q1: {sum(lines)}")
 
def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day9.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character, lines))
    lines = list(map(convert_to_int_list, lines))

    lines = list(map(subtract_part_2, lines))
    logger.info(f"Sum of these extrapolated values Q2: {sum(lines)}")
    

if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()