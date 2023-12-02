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

def convert_to_tuple(val):
    val = str(val).strip().split(",")

    cube_set_main = []
    for each_val in val:
        each_val = each_val.strip().split(" ")
        num = int(each_val[0])
        color = each_val[1]
        cube_set = (num, color)
        cube_set_main.append(cube_set)
    
    return cube_set_main

def separate_key_values(val:str):
    val_list = str(val).split(":")
    values = str(val_list[1]).strip()
    split_values = values.split(";")
    tuple_list = list(map(convert_to_tuple, split_values))

    key = int(val_list[0].split(" ")[1])
    obj = {
        key: tuple_list
    }
    
    return obj

def check_possible_condition(val:dict, possible_condition:list):

    key = 0
    conditions_fullfilled = []

    for key in val.keys():
        values = val[key]
        for each_set_value in values:
            for each_condition in possible_condition:
                for each_subset in each_set_value:
                    if each_condition[1] == each_subset[1]:

                        if each_subset[0] <= each_condition[0]:
                            conditions_fullfilled.append(True)
                        else:
                            conditions_fullfilled.append(False)
                       
    if all(conditions_fullfilled) == True:
        return True

def get_keys(val:dict):
    for key, value in val.items():
        return key

def check_fewest_number_of_cubes(val:dict):
    
    cube_colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for key, value in val.items():
        for each_set in value:
            for each_subset in each_set:
                color = each_subset[1]
                cube_number = each_subset[0]

                if cube_number >= cube_colors[color]:
                        cube_colors[color] = cube_number  

    reduced_vals = 1
    for k,v in cube_colors.items():
        reduced_vals *= v

    return reduced_vals

# ---------





possible_condition = [(12, 'red'), (13, 'green'), (14, 'blue')]

def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day2.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    list_of_dict = list(map(separate_key_values, lines))
    filtered = list(filter(lambda x: check_possible_condition(x, possible_condition), list_of_dict))
    game_ids = list(map( get_keys , filtered))
    sum_of_ids_of_games = sum(game_ids)
    logger.info(f"Sum of IDs of game Q1: {sum_of_ids_of_games}")

def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day2.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    list_of_dict = list(map(separate_key_values, lines))
    reduced_values = list(map(check_fewest_number_of_cubes, list_of_dict))
    final_answer = sum(reduced_values)
    logger.info(f"Sum of Power of these sets Q2: {final_answer}")



if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()