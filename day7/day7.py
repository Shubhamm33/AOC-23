import os
from logger import logger
import time

single_card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', 
'3', '2']

# single_card_order_joker = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', 
# '3', '2', 'J']

single_card_order_joker = ['J', '2','3','4','5','6','7','8','9','T','Q', 'K','A']

# utils---
def remove_new_line_character(val:str):
    newline_character = str(val).endswith("\n")
    if newline_character:
        val = str(val).removesuffix("\n")
        return val
    else:
        return val

def examine_hand(_hand, part=None):
    user = _hand.split(" ")
    _hand = user[0]
    _bid = int(user[1])

    # first = _hand[0]
    hand_metdata = {
        'is_five_of_a_kind': None,
        'is_four_of_a_kind': None,
        'is_full_house': None,
        'is_three_of_a_kind': None,
        'is_two_pair': None,
        'is_one_pair': None,
        'is_high_card': None,
        'hand': _hand,
        'bid': _bid,
        'rank': 0,
        'label_sort': 0
    }


    five_kind_check = []
    four_kind_check = []    
    full_house = []
    three_kind_check = [] 
    two_pair_check = [] 
    one_pair_check = [] 

    if part is None:
        # Five kind
        for i in range(len(_hand)):
            five_kind_check.append(check_five_of_kind(_hand[i], _hand))
        hand_metdata['is_five_of_a_kind'] = True if five_kind_check.count(True) == 5 else False
        if hand_metdata['is_five_of_a_kind']:
            hand_metdata['label_sort'] = 1
            return hand_metdata

        # # Four kind
        if hand_metdata['is_five_of_a_kind'] == False:
            for i in range(len(_hand)):
                four_kind_check.append(check_four_of_kind(_hand[i], _hand))
            hand_metdata['is_four_of_a_kind'] = True if four_kind_check.count(True) == 4 and four_kind_check.count(False) == 1 else False
            if hand_metdata['is_four_of_a_kind']:
                hand_metdata['label_sort'] = 2
                return hand_metdata
        
        # Full house
        if hand_metdata['is_four_of_a_kind'] == False:
            for i in range(len(_hand)):
                full_house.append(check_full_house(_hand[i], _hand))
            hand_metdata['is_full_house'] = True if full_house.count(3) == 3 and full_house.count(2) == 2 else False
            if hand_metdata['is_full_house']:
                hand_metdata['label_sort'] = 3
                return hand_metdata

        # Three kind
        if hand_metdata['is_full_house'] == False:
            for i in range(len(_hand)):
                three_kind_check.append(check_three_of_kind(_hand[i], _hand))
            hand_metdata['is_three_of_a_kind'] = True if three_kind_check.count(True) == 3 and three_kind_check.count(False) == 2 else False
            if hand_metdata['is_three_of_a_kind']:
                hand_metdata['label_sort'] = 4
                return hand_metdata

        # Two Pair
        if hand_metdata['is_three_of_a_kind'] == False:
            for i in range(len(_hand)):
                two_pair_check.append(check_two_pair(_hand[i], _hand))
            hand_metdata['is_two_pair'] = two_pair_occurence(two_pair_check)
            if hand_metdata['is_two_pair']:
                hand_metdata['label_sort'] = 5
                return hand_metdata
        
        # One Pair
        if hand_metdata['is_two_pair'] == False:
            for i in range(len(_hand)):
                one_pair_check.append(check_one_pair(_hand[i], _hand))
            hand_metdata['is_one_pair'] = one_pair_occurence(one_pair_check)
            if hand_metdata['is_one_pair']:
                hand_metdata['label_sort'] = 6
                return hand_metdata
        
        # High Card
        if hand_metdata['is_one_pair'] == False:
            hand_metdata['is_high_card'] = True
            hand_metdata['label_sort'] = 7
            return hand_metdata
        
        logger.warning("\n")
    
    else:

        return (_hand, _bid)

        # Five kind
        # for i in range(len(_hand)):
        #     five_kind_check.append(check_five_of_kind(_hand[i], _hand, part))

        # hand_metdata['is_five_of_a_kind'] = True if five_kind_check.count(True) == 5 else False
        # if hand_metdata['is_five_of_a_kind']:
        #     hand_metdata['label_sort'] = 1
        #     return hand_metdata

        # # # Four kind
        # if hand_metdata['is_five_of_a_kind'] == False:

        #     _hand = replace_joker_with_maximum(_hand)

        #     for i in range(len(_hand)):
        #         if _hand[i] != 'J':
        #             four_kind_check.append(check_four_of_kind(_hand[i], _hand, part))

        #     hand_metdata['is_four_of_a_kind'] = True if four_kind_check.count(True) == 4 and four_kind_check.count(False) == 1 else False
        #     if hand_metdata['is_four_of_a_kind']:
        #         hand_metdata['label_sort'] = 2
        #         return hand_metdata
        

        # # Full house
        # if hand_metdata['is_four_of_a_kind'] == False:
        #     for i in range(len(_hand)):
        #         full_house.append(check_full_house(_hand[i], _hand, '2'))
        #     hand_metdata['is_full_house'] = True if full_house.count(3) == 3 and full_house.count(2) == 2 else False
        #     if hand_metdata['is_full_house']:
        #         hand_metdata['label_sort'] = 3
        #         return hand_metdata

        # # Three kind
        # if hand_metdata['is_full_house'] == False:
        #     for i in range(len(_hand)):
        #         three_kind_check.append(check_three_of_kind(_hand[i], _hand, '2'))
        #     hand_metdata['is_three_of_a_kind'] = True if three_kind_check.count(True) == 3 and three_kind_check.count(False) == 2 else False
        #     if hand_metdata['is_three_of_a_kind']:
        #         hand_metdata['label_sort'] = 4
        #         return hand_metdata


def eval_joker_hand(hand):
    values = [card for card in hand[0]]

    if any(values.count(value) == 5 for value in set(values)):
        hand_value = 7
    elif any(values.count(value) == 4 for value in set(values)):
        if values.count('J') in [1, 4]:
            hand_value = 7
        else:
            hand_value = 6
    elif any(values.count(value) == 3 for value in set(values)) and any(values.count(value) == 2 for value in set(values)):
        if values.count('J') in [2, 3]:
            hand_value = 7
        else:
            hand_value = 5
    elif any(values.count(value) == 3 for value in set(values)):
        if values.count('J') in [1, 3]:
            hand_value = 6
        else:
            hand_value = 4
    # elif sum(values.count(value) == 2 for value in set(values)) == 2:
    elif len([1 for value in set(values) if values.count(value) == 2]) == 2:
        if values.count('J') == 1:
            hand_value = 5
        elif values.count('J') == 2:
            hand_value = 6
        else:
            hand_value = 3
    elif any(values.count(value) == 2 for value in set(values)):
        if values.count('J') in [1, 2]:
            hand_value = 4
        else:
            hand_value = 2
    else:
        if values.count('J') == 1:
            hand_value = 2
        else:
            hand_value = 1
    # print(hand[0], hand_value)
    return hand_value
    


def check_five_of_kind(char, hand, part=None):
    # five_of_a_kind = False
    is_five_of_a_kind = []    

    if part is None:
        for i in range(len(hand)):
            if char == hand[i]:
                is_five_of_a_kind.append(True)
            else:
                is_five_of_a_kind.append(False)

        if all(is_five_of_a_kind) == True:
            return True
        else:
            return False
    
    else:
        for i in range(len(hand)):

            if (char == 'J') or (char == hand[i]) or (hand[i] == 'J'):
                is_five_of_a_kind.append(True)
            else:
                is_five_of_a_kind.append(False)

        if all(is_five_of_a_kind) == True:
            return True
        else:
            return False

def check_four_of_kind(char, hand, part=None):
    is_four_of_a_kind = []

    if part is None:
        for i in range(len(hand)):
            if char == hand[i]:
                is_four_of_a_kind.append(True)
            else:
                is_four_of_a_kind.append(False)

        true_count = is_four_of_a_kind.count(True)
        false_count = is_four_of_a_kind.count(False)

        return True if true_count == 4 and false_count == 1 else False
    
    else:
        for i in range(len(hand)):
            if char == hand[i]:
                is_four_of_a_kind.append(True)
            else:
                is_four_of_a_kind.append(False)

        true_count = is_four_of_a_kind.count(True)
        false_count = is_four_of_a_kind.count(False)

        return True if true_count == 4 and false_count == 1 else False

def check_full_house(char, hand, part=None):
    arr = []
    if part is None:
        for i in range(len(hand)):
            if char == hand[i]:
                arr.append(i)
        # logger.info(f"{char} {len(arr)}")
        return len(arr)
    else:
        for i in range(len(hand)):
            if char == hand[i]:
                arr.append(i)
            
        # logger.info(f"{char} {len(arr)}")
        return len(arr)

def check_three_of_kind(char, hand, part=None):
    is_three_of_a_kind = []    
    if part is None:
        for i in range(len(hand)):
            if char == hand[i]:
                is_three_of_a_kind.append(True)
            else:
                is_three_of_a_kind.append(False)

        true_count = is_three_of_a_kind.count(True)
        false_count = is_three_of_a_kind.count(False)

        return True if true_count == 3 and false_count == 2 else False
    else:
        for i in range(len(hand)):
            if char == 'J':
                is_three_of_a_kind.append(True)
            elif (char == hand[i]) or (hand[i] == 'J'):
                is_three_of_a_kind.append(True)
            else:
                is_three_of_a_kind.append(False)

        true_count = is_three_of_a_kind.count(True)
        false_count = is_three_of_a_kind.count(False)

        return True if true_count == 3 and false_count == 2 else False



def check_two_pair(char, hand, part=None):
    arr = []
    for i in range(len(hand)):
        if (char == 'J') or (char == hand[i]) or (hand[i] == 'J'):
            arr.append(i)

    return char, len(arr)

def two_pair_occurence(two_pair_check, part=None):

    char_list = []
    for c, o in two_pair_check:
        if o == 2 :
            char_list.append(c)

    return True if len(set(char_list)) == 2 else False

def check_one_pair(char, hand, part=None):
    arr = []
    for i in range(len(hand)):
        if (char == 'J') or (char == hand[i]) or (hand[i] == 'J'):
            arr.append(i)

    return char, len(arr)

def one_pair_occurence(one_pair_check, part=None):
    char_list = []
    for c, o in one_pair_check:
        if o == 2:
            char_list.append(c)
    return True if len(set(char_list)) == 1 else False






def map_values_to_numeric(val):
    for k, v in val.items():
        if v == True:
            val[k] = 1
        elif v == False or v == None:
            val[k] = 0
    
    return val

def check_sorting(all_hands, method):

    try:
        arr = [v for v in all_hands if v.get(method)]

        for i in range(len(arr)):

            for j in range(len(arr)):

                if arr[i]['hand'] != arr[j]['hand']:

                    h1 = arr[i]['hand']
                    h2 = arr[j]['hand']

                    for r in range(len(h1)):
                        index_1 = single_card_order.index(h1[r])
                        index_2 = single_card_order.index(h2[r])
                        if index_1 > index_2:
                            temp = arr[i]
                            arr[i] = arr[j]
                            arr[j] = temp
                            break
                        elif index_2 > index_1:
                            break

    except:
        logger.error('Err', exc_info=True)

    arr.reverse()
    return arr

def solve_puzzle_part_1():
    path = os.path.join(os.getcwd(), 'day7.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')
    with open(path, 'r') as f:
        lines = f.readlines()

    lines = list(map(remove_new_line_character, lines))

    all_hands = list(map(examine_hand, lines))
    all_hands = list(map(map_values_to_numeric, all_hands))
    all_hands = sorted(all_hands, key=lambda x: x['label_sort'])

    five_kinds = check_sorting(all_hands, 'is_five_of_a_kind')
    four_kinds = check_sorting(all_hands, 'is_four_of_a_kind')
    full_house = check_sorting(all_hands, 'is_full_house')
    three_kinds = check_sorting(all_hands, 'is_three_of_a_kind')
    two_pair = check_sorting(all_hands, 'is_two_pair')
    one_pair = check_sorting(all_hands, 'is_one_pair')
    high_card = check_sorting(all_hands, 'is_high_card')

    sorted_list = five_kinds + four_kinds + full_house + three_kinds + two_pair + one_pair + high_card
    sorted_list.reverse()

    total_winnings = 0
    for counter, i in enumerate(sorted_list):
        total_winnings += (counter + 1) * i['bid']
    
    logger.info(f"Total Winnings Q1: {total_winnings}")

def solve_puzzle_part_2():
    path = os.path.join(os.getcwd(), 'day7.txt')
    # path = os.path.join(os.getcwd(), 'test.txt')
    with open(path, 'r') as f:
        lines = f.readlines()

    lines = list(map(remove_new_line_character, lines))
    all_hands = list(map(lambda x : examine_hand(x, '2'), lines))

    cards_sorted = sorted(all_hands, key=lambda x: ( eval_joker_hand(x), [single_card_order_joker.index(card) for card in x[0] ] ))

    total_winnings = 0
    for counter, r in enumerate(cards_sorted):
        total_winnings += (counter + 1) * r[1]
    
    logger.info(f"Total winnings Q2: {total_winnings}")

if __name__ == '__main__':
    solve_puzzle_part_1()
    solve_puzzle_part_2()