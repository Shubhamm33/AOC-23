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

def split_into_dict(val:str):
    val_list = val.split(" = ")
    key = val_list[0]
    value = val_list[1]
    value = tuple(str(value[1:-1]).split(", "))

    obj = {
        key: value
    }

    return obj

def find_road_network(lines_dict:list, rule):
    # logger.info(len(rule[:-1]))

    reached = False
    counter = 0
    start = 'AAA'

    """
    current = map_dict[current][LR_MAP[directions[dir_index]]
    
    while directions is the full LRRLRLLRR thing and the dir_index is basically same as the counter - except for when the dir_index reaches len(directions), then it resets to 0. And LR_MAP is my L: 0, R:1 mapping
    """

    while not reached:

        for move in rule[:-1]:

            counter += 1

            v = list(filter(lambda x : x if start in x.keys() else False, lines_dict))[0][start]
            
            # logger.info(f"Move:{move} Start:{start} {v}")

            if move == "L":
                start = v[0]
            elif move == 'R':
                start = v[1]

            if start == 'ZZZ':
                reached=True

    return counter

def filter_by_last(val, start):
    if start == list(val.keys())[0][-1]:
        return True
    return False   

def find_road_network_2(lines_dict:list, rule):
    # logger.info(lines_dict)
    combined_dict={}

    # Iterate through the list of dictionaries
    for dictionary in lines_dict:
        # Update the combined_dict with key-value pairs from the current dictionary
        combined_dict.update(dictionary)

    start_positions = [key for key in combined_dict if key.endswith("A")]
    end_positions = [key for key in combined_dict if key.endswith("Z")]

    logger.info(start_positions)
    logger.info(end_positions)
    """
    current = map_dict[current][LR_MAP[directions[dir_index]]
    
    while directions is the full LRRLRLLRR thing and the dir_index is basically same as the counter - except for when the dir_index reaches len(directions), then it resets to 0. And LR_MAP is my L: 0, R:1 mapping
    """
    all_combs = []
    try:
        rule = rule[:-1]
        for s_pos in start_positions:
            counter = 0
            reached = False
            start = s_pos
            logger.info(start)
            a_to_z_combination = {}

            while not reached:

                for move in rule:
                    counter += 1
                    v = list(filter(lambda x : x if start in x.keys() else False, lines_dict))[0][start]

                    if move == "L":
                        start = v[0]
                    elif move == 'R':
                        start = v[1]

                    # logger.info(f"Move:{move} Start:{start} {v}")

                    if start in end_positions:
                        a_to_z_combination['start_position'] = s_pos
                        a_to_z_combination['counter'] = counter
                        a_to_z_combination['end_position'] = start
                        all_combs.append(a_to_z_combination)
                        reached = True
                        counter = 0
                        break
 
    except:
        logger.error("ERR", exc_info=True)

    
    # c = 0
    # for comb in all_combs:
    #     c = c+comb['counter']
    #     logger.info(comb)
    # logger.info(c)

    return all_combs

def find_road_network_2_by_donoglas(combined_dict:list, rule):
    starting_labels = [
        label
        for label
        in combined_dict.keys()
        if label.endswith("A")
    ]
    logger.info(f"starting_labels: {len(starting_labels)} {starting_labels}")
    
    ending_labels = [
        label
        for label
        in combined_dict.keys()
        if label.endswith("Z")
    ]
    logger.info(f"ending_labels: {len(ending_labels)} {ending_labels}")
    
    all_cycles = []

    for label in starting_labels:
        found_z = None
        current_cycle = []
        current_cycle_steps = 0
        current_cycle_instructions = rule[:-1]

        while True:
            while current_cycle_steps == 0 or not label.endswith("Z"):
                current_cycle_steps += 1
                label = combined_dict[label][0 if current_cycle_instructions[0] == 'L' else 1]
                current_cycle_instructions = current_cycle_instructions[1:] + current_cycle_instructions[0]

            current_cycle.append(current_cycle_steps)

            if found_z is None:
                found_z = label
                all_cycles.append(current_cycle_steps)
                current_cycle_steps = 0
            elif found_z == label:
                all_cycles.append(current_cycle_steps)
                break
            elif found_z in ending_labels:
                all_cycles.append(current_cycle_steps)
                current_cycle_steps = 0

    logger.info(all_cycles)

def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day8.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        rule = f.readline()
        lines = f.readlines()
    lines = list(map(remove_new_line_character, lines))[1:]
    lines_dict = list(map(split_into_dict, lines))

    steps = find_road_network(lines_dict, rule)
    logger.info(f"Steps taken Q1: {steps}")
    
def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day8.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        rule = f.readline()
        lines = f.readlines()
    
    lines = list(map(remove_new_line_character, lines))[1:]
    lines_dict = list(map(split_into_dict, lines))


    # logger.info(lines_dict)
    combined_dict={}

    # Iterate through the list of dictionaries
    for dictionary in lines_dict:
        # Update the combined_dict with key-value pairs from the current dictionary
        combined_dict.update(dictionary)

    combinations = find_road_network_2(lines_dict, rule)
    # steps = find_road_network_2_by_donoglas(combined_dict, rule)

    counters = [c['counter'] for c in combinations]
    lcm = math.lcm(*counters)
    steps = lcm
    logger.info(f"Steps taken Q2: {steps}")



if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()