import os, time, re
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

def make_dict_objects(numbers):
    obj=dict()
    for counter, n in enumerate(numbers):
        if counter == 0:
            obj['destination'] = n
        elif counter == 1:
            obj['source'] = n
        elif counter == 2:
            obj['range'] = n
        
    obj['mapping'] = np.zeros((obj['range'], 2))
    return obj

def get_seeds(seeds):
    seeds = list(map(remove_new_line_character , [seeds])) 
    seeds = [ int(seed_num) for seed_num in seeds[0].split(":")[1].strip().split(" ") ]
    return seeds

def add_mapping(obj):

    for key, value in obj.items():
        for each_row in value:
            
            source = [i for i in range(each_row['source'], each_row['source'] + each_row['range']) ]
            source = np.array(source)

            destination = [i for i in range(each_row['destination'], each_row['destination'] + each_row['range']) ]
            destination = np.array(destination)

            each_row['mapping'] = np.hstack( (source.reshape(-1,1), destination.reshape(-1,1)) )

    return obj

def get_mappings(lines):
    lines = list(map(remove_new_line_character , lines))
    lines = list(filter(lambda x : x != '' , lines))

    pattern = r'\b\d+\b'
    key = ''
    obj = dict()
    for line in lines:
        numbers = re.findall(pattern, line)
        if numbers:
            numbers = [int(n) for n in numbers]
            number_mapping = make_dict_objects(numbers)
            obj[key].append(number_mapping)
        else:
            key = line.split(" ")[0]
            obj[key] = []

    obj = add_mapping(obj)

    return obj

def get_mapped_transfer_value(mappings, prev_value, label):

    mapped_data = []
    
    result_data = []

    for key, value in mappings.items():
        if key == label:
            mapped_data = value


    for num in prev_value:

        result = []
        for each_rule in mapped_data:
            is_present = np.where(each_rule['mapping'][:,0] == num)
            if len(is_present[0]) != 0:
                index = is_present[0][0]
                val = each_rule['mapping'][index][1]
                result.append(val)

        if len(result) == 0:
            result.append(num)

        result_data.append(result)
    
    result_data = [ n[0] for n in result_data ]
    return result_data


#  -----


def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day5.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        seeds = f.readline()
        seeds = get_seeds(seeds)

        lines = f.readlines()

        lines = ''.join(lines)
        lines = lines.split("\n\n")


    for each_block in lines:
        each_block = [ n for n in each_block.split("\n") if n != '' ][1:]

        new = []

        for seed in seeds:
            check_value = seed
            for each_rule in each_block:
                destination, source, range_value = map(int, each_rule.split())

                if source <= check_value <= (source + range_value) - 1:
                    
                    diff = check_value - int(source)
                    found_value = destination + diff
                    new.append(found_value)
                    break
            else:
                found_value = check_value
                new.append(found_value)

        seeds = new

    answer = min(new)
    logger.info(f"Q1: {answer}")
    
    
def solve_puzzle_part_2():

    path = os.path.join(os.getcwd(), 'day5.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        seeds = f.readline()
        seeds = get_seeds(seeds)

        lines = f.readlines()

        lines = ''.join(lines)
        lines = lines.split("\n\n")

    # logger.info(seeds)

    seed_range = []
    for i in range(0, len(seeds), 2):
        seed_range.append((seeds[i], seeds[i] + seeds[i+1]))
    
    # logger.info(seed_range)
    seeds = seed_range

    for each_block in lines:
        each_block = [ n for n in each_block.split("\n") if n != '' ][1:]

        new = []

        while len(seeds) > 0:
            start_val, end_val = seeds.pop()

            for each_rule in each_block:
                destination, source, range_value = map(int, each_rule.split())

                overlap_start = max(start_val, source)
                overlap_end = min(end_val, source + range_value)

                if overlap_start < overlap_end:
                    new.append( (overlap_start - source + destination, overlap_end - source + destination) )

                    if overlap_start > start_val:
                        seeds.append((start_val, overlap_start))
                    if end_val > overlap_end:
                        seeds.append((overlap_end, end_val))
                    break
            else:
                new.append((start_val, end_val))
                    
        seeds = new

    # logger.info(seeds)
    answer = min(seeds)[0]
    logger.info(f"Q2: {answer}")
    


if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()