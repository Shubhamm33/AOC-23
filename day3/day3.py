import os
from logger import logger
import pandas as pd
import numpy as np
import time

# utils---
def remove_new_line_character(val:str):
    newline_character = str(val).endswith("\n")
    if newline_character:
        val = str(val).removesuffix("\n")
        return val
    else:
        return val

def separate_each_character(val):
    character_l = []
    for each_val in val:
        character_l.append(each_val)
    return character_l

def find_symbol_adjacents(arr):

    adj_arr = []

    for i_counter, i in enumerate(arr):

        for j_counter, j in enumerate(i):
            
            if (str(j).isdigit() == False) and (j != '.'): 
                
                symbol_arr = []

                obj = {
                    'value': j,
                    'coords': (i_counter, j_counter)
                }

                left_element = get_left_element(i_counter, j_counter, arr)
                left_top_element = get_adj_left_top_element(i_counter, j_counter, arr)
                top_element = get_top_element(i_counter, j_counter, arr)
                right_top_element = get_adj_right_top_element(i_counter, j_counter, arr)
                right_element = get_right_element(i_counter, j_counter, arr)
                right_bottom_element = get_adj_right_bottom_element(i_counter, j_counter, arr)
                bottom_element = get_bottom_element(i_counter, j_counter, arr)
                left_bottom_element = get_adj_left_bottom_element(i_counter, j_counter, arr)

                symbol_arr.append(obj)
                
                if left_element['value'] != '.':
                    symbol_arr.append(left_element)
                if left_top_element['value'] != '.':
                    symbol_arr.append(left_top_element)
                if top_element['value'] != '.':
                    symbol_arr.append(top_element)
                if right_top_element['value'] != '.':
                    symbol_arr.append(right_top_element)
                if right_element['value'] != '.':
                    symbol_arr.append(right_element)
                if right_bottom_element['value'] != '.':
                    symbol_arr.append(right_bottom_element)
                if bottom_element['value'] != '.':
                    symbol_arr.append(bottom_element)
                if left_bottom_element['value'] != '.':
                    symbol_arr.append(left_bottom_element)

                adj_arr.append(symbol_arr)

    return adj_arr

def get_left_element(i, j, arr):
    obj = {
        'value': arr[i][j-1],
        'coords': (i, j-1)
    }
    return obj

def get_right_element(i, j, arr):
    obj = {
        'value': arr[i][j+1],
        'coords': (i, j+1)
    }
    return obj

def get_top_element(i, j, arr):
    obj = {
        'value': arr[i-1][j],
        'coords': (i-1, j)
    }
    return obj

def get_bottom_element(i, j, arr):
    obj = {
        'value': arr[i+1][j],
        'coords': (i+1, j)
    }
    return obj

def get_adj_left_top_element(i, j, arr):
    obj = {
        'value': arr[i-1][j-1],
        'coords': (i-1, j-1)
    }
    return obj

def get_adj_right_top_element(i, j, arr):
    obj = {
        'value': arr[i-1][j+1],
        'coords': (i-1, j+1)
    }
    return obj

def get_adj_left_bottom_element(i, j, arr):
    obj = {
        'value': arr[i+1][j-1],
        'coords': (i+1, j-1)
    }
    return obj

def get_adj_right_bottom_element(i, j, arr):
    obj = {
        'value': arr[i+1][j+1],
        'coords': (i+1, j+1)
    }
    return obj

def find_complete_number(num:dict, arr:list, coords_used):

    try:
        i = num['coords'][0]
        j = num['coords'][1]

        
        numbers_left, coords_used = find_left_num(i, j, coords_used, arr)
        numbers_left = list(reversed(numbers_left)) 

        numbers_right, coords_used = find_right_num(i, j, coords_used, arr)

        final_num = numbers_left + numbers_right

        return final_num


    except KeyboardInterrupt:
        logger.error('User exited', exc_info=True)
    except:
        logger.error('ERR', exc_info=True)
    
    return None

def find_left_num(i, j, coords_used, arr):

    numbers = []

    obj = {
        'value': arr[i][j],
        'coords': (i, j)
    }

    numbers.append(obj)

    going_left = True
    while going_left:
        if j < 0:
            going_left = False
        else:

            j -= 1
            num = arr[i][j]

            if str(num).isdigit():
                obj = {
                    'value': num,
                    'coords': (i, j)
                }

                if obj['coords'] not in coords_used:
                    coords_used.append(obj['coords'])
                    numbers.append(obj)

            else:
                going_left = False 
    
    return numbers, coords_used

def find_right_num(i, j, coords_used, arr):
    shapeY = arr.shape[1] - 1

    numbers = []

    going_right = True
    while going_right:

        if j >= shapeY:
            going_right = False

        else:
        
            j += 1
            num = arr[i][j]

            if str(num).isdigit():
                obj = {
                    'value': num,
                    'coords': (i, j)
                }
                if obj['coords'] not in coords_used:
                    coords_used.append(obj['coords'])
                    numbers.append(obj)
            else:
                going_right = False

    return numbers, coords_used

def combine_string_value_convert_integer(final_num):
    num = [v['value'] for v in final_num]
    num = int(''.join(num))
    # logger.info(num)
    return num


# utils for solution 2 --------
def get_star_gear_adjacents(arr):
    
    adj_arr = []

    for i_counter, i in enumerate(arr):

        for j_counter, j in enumerate(i):
            
            if (str(j).isdigit() == False) and (j != '.') and (j == '*'): 
                
                symbol_arr = []

                obj = {
                    'value': j,
                    'coords': (i_counter, j_counter)
                }

                left_element = get_left_element(i_counter, j_counter, arr)
                left_top_element = get_adj_left_top_element(i_counter, j_counter, arr)
                top_element = get_top_element(i_counter, j_counter, arr)
                right_top_element = get_adj_right_top_element(i_counter, j_counter, arr)
                right_element = get_right_element(i_counter, j_counter, arr)
                right_bottom_element = get_adj_right_bottom_element(i_counter, j_counter, arr)
                bottom_element = get_bottom_element(i_counter, j_counter, arr)
                left_bottom_element = get_adj_left_bottom_element(i_counter, j_counter, arr)

                symbol_arr.append(obj)
                
                if left_element['value'] != '.':
                    symbol_arr.append(left_element)
                if left_top_element['value'] != '.':
                    symbol_arr.append(left_top_element)
                if top_element['value'] != '.':
                    symbol_arr.append(top_element)
                if right_top_element['value'] != '.':
                    symbol_arr.append(right_top_element)
                if right_element['value'] != '.':
                    symbol_arr.append(right_element)
                if right_bottom_element['value'] != '.':
                    symbol_arr.append(right_bottom_element)
                if bottom_element['value'] != '.':
                    symbol_arr.append(bottom_element)
                if left_bottom_element['value'] != '.':
                    symbol_arr.append(left_bottom_element)

                adj_arr.append(symbol_arr)

    return adj_arr


# -------------

def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day3.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    lines = list(map(separate_each_character , lines))
    lines_arr = np.array(lines)

    logger.info(f"\n{lines_arr}")

    adj_arrays = find_symbol_adjacents(lines_arr)

    coordinates_used = []

    all_part_numbers_in_engine = []

    for arr in adj_arrays:
        for each_num in arr:
            if str(each_num['value']).isdigit():

                if each_num['coords'] not in coordinates_used:

                    coordinates_used.append(each_num['coords'])
                    final_num = find_complete_number(each_num, lines_arr, coordinates_used)
                    final_num =  combine_string_value_convert_integer(final_num)

                    all_part_numbers_in_engine.append(final_num)

    answer = sum(all_part_numbers_in_engine)
    
    logger.info(f"Sum of all the part numbers in engine schematic Q1: {answer}")

def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day3.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character , lines))
    lines = list(map(separate_each_character , lines))
    lines_arr = np.array(lines)

    logger.info(f"\n{lines_arr}")
    adj_arr = get_star_gear_adjacents(lines_arr)

    coordinates_used = []

    all_part_numbers_in_engine = []

    final_num = None

    for arr in adj_arr:
        
        gear_ratios = []

        for each_num in arr:

            if str(each_num['value']).isdigit():

                if each_num['coords'] not in coordinates_used:
                    coordinates_used.append(each_num['coords'])

                    final_num = find_complete_number(each_num, lines_arr, coordinates_used)
                
                else:
                    final_num = None
            else:
                final_num = None

            gear_ratios.append(final_num)

        gear_ratios = [v for v in gear_ratios if v is not None]
        if len(gear_ratios) == 2:
            all_part_numbers_in_engine.append(gear_ratios)

    ans_list = []
    for g in all_part_numbers_in_engine:
        
        final_number = []
        
        for num in g:
            num = [n['value'] for n in num]
            num = int(''.join(num))
            final_number.append(num)
        
        n = final_number[0] * final_number[1]
        ans_list.append(n)

    answer = sum(ans_list)
    
    logger.info(f"Sum of all the gear numbers in engine schematic Q2: {answer}")

if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()