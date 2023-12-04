import os, time
from logger import logger
import numpy as np

# utils---
def remove_new_line_character(val:str):
    newline_character = str(val).endswith("\n")
    if newline_character:
        val = str(val).removesuffix("\n")
        return val
    else:
        return val

def get_points_each_card(val:str):
    new_val = str(val).split(":")
    # key = new_val[0]
    value = str(new_val[1]).strip()
    value = value.split('|')

    winning_numbers = str(value[0]).strip().split(" ")
    my_numbers = str(value[1]).strip().split(" ")

    winning_numbers = [n for n in winning_numbers if n != '']
    my_numbers = [n for n in my_numbers if n != '']

    points = check_my_number_in_winning_number(winning_numbers, my_numbers)
    return points

def check_my_number_in_winning_number(win_nums, my_nums):
    points = 0
    initial = True
    for n in my_nums:
        if n in win_nums:
            if initial:
                points += 1
                initial = False
            else:
                points *= 2

    # logger.info(f"Points: {points}")

    return points


# puzzle 2:
def convert_to_dict(val):
    new_val = str(val).split(":")
    key = new_val[0]
    value = str(new_val[1]).strip()
    value = value.split('|')

    winning_numbers = str(value[0]).strip().split(" ")
    my_numbers = str(value[1]).strip().split(" ")

    winning_numbers = [n for n in winning_numbers if n != '']
    my_numbers = [n for n in my_numbers if n != '']

    value = [winning_numbers, my_numbers]
    obj = {
        key: value
    }
    return obj

def get_matching_number(win_nums, my_nums):
    matching_nums = 0

    for n in my_nums:
        if n in win_nums:
            matching_nums += 1

    return matching_nums

def find_card_copy(key:str, vals):
    for counter, card in enumerate(vals):
        for k, v in card.items():
            logger.info(f"{k} {key}")
            if k == key:
                return counter, card

    # return 0, 'CPOT'

def get_copies_and_process(vals:list):

    list_counter = 0
    list_end = False
    copies = np.ones(len(vals))

    while not list_end:

        try:
            d = dict(vals[list_counter])

            for k,v in d.items():
                win_nums = v[0]
                my_nums = v[1]

            matching_nums = get_matching_number(win_nums, my_nums)

            
            for i in range(1, matching_nums+1):
                copies[list_counter+i] += copies[list_counter]

        except KeyboardInterrupt:
            logger.error('User exited')
            list_end = True
        except:
            list_end = True

        list_counter += 1

    return copies
# -------------

def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day4.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    points = list(map(get_points_each_card, lines))

    answer = sum(points)
    logger.info(f"Points worth in total Q1: {answer}")

def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day4.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    list_of_dicts = list(map(convert_to_dict, lines))

    total_cards = get_copies_and_process(list_of_dicts)

    answer = int(sum(total_cards))
    logger.info(f"Total scratchcards we end up with Q2: {answer}")

if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()