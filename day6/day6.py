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

def get_list_remove_space(val, whichPart = None):
    if whichPart == 'part2':
        val = val.split(' ')
        val = [v for v in val if v != '']
        new_val = ''
        for v in val:
            new_val += v

        return new_val
    else:
        val = val.split(' ')
        val = [int(v) for v in val if v != '']
        return val
#  -----

def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day6.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()

    lines = list(map(remove_new_line_character, lines))
    logger.info(lines)

    time = None
    distance = None
    for counter, line in enumerate(lines):
        if counter == 0:
            time = line.split(":")[1].strip()
        else:
            distance = line.split(":")[1].strip()

    time = get_list_remove_space(time)
    distance = get_list_remove_space(distance)
    timendistance = list(zip(time, distance))

    beat_the_record = 1

    for i in timendistance:
        race_won = 0
        for time in range(i[0] + 1):
            total_distance_travelled = (i[0] - time) * time 
            if total_distance_travelled > i[1]:
                race_won += 1

        beat_the_record *= race_won

    logger.info(f"Race won Q1: {beat_the_record}")

def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day6.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')

    with open(path, 'r') as f:
        lines = f.readlines()

    lines = list(map(remove_new_line_character, lines))
    logger.info(lines)

    time = None
    distance = None
    for counter, line in enumerate(lines):
        if counter == 0:
            time = line.split(":")[1].strip()
        else:
            distance = line.split(":")[1].strip()

    time = get_list_remove_space(time, 'part2')
    distance = get_list_remove_space(distance, 'part2')

    time = int(time)
    distance = int(distance)

    timendistance = list(zip([time], [distance]))

    beat_the_record = 1

    for i in timendistance:
        race_won = 0
        for time in range(i[0] + 1):
            total_distance_travelled = (i[0] - time) * time 
            if total_distance_travelled > i[1]:
                race_won += 1

        beat_the_record *= race_won

    logger.info(f"Race won Q2: {beat_the_record}")


if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()