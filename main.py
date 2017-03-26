import collections
import itertools
from config import keypad

def count_key_press(input):
    # a dictionary where key is the unique char and
    # value is the number of times that the char appears in the word
    char_count_dict = collections.Counter(input)

    # convert to list of tuples where each tuple indicate the char and n
    char_count = sorted(char_count_dict.items())

    n_press = 0
    for char_pair in char_count:
        char = char_pair[0]
        count = char_pair[1]
        # find the index of the char in the number that contains the char
        for key, value in keypad.iteritems():
            if char in value:
                index = value.index(char) + 1
                break
        n_press += index * count
    return n_press

##print count_key_press('hello')
#13
##print count_key_press('wonderful')
#20

def number_pressed(input):
    key_pressed = ''
    for char in input:
        # find the number that contains the char
        for key, value in keypad.iteritems():
            if char in value:
                key_pressed += key
                break
    return int(key_pressed)

##print number_pressed('hello')
#43556
##print number_pressed('wonderful')
#966337385

def all_combinations(input):
    input = str(input)

    # base condition: if only one char, return all chars corresponding to the number
    if len(input) == 1:
        return keypad[input]
    else:
        first = keypad[input[0]]
        prev = all_combinations(input[1:])
        # add each of the char corresponds to first number to every combinations from the rest numbers
        combined = map(lambda x: map(lambda y: x + y, prev), first)
        # flatten the list
        combined_flat = list(itertools.chain.from_iterable(combined))
    return combined_flat

##print all_combinations(23)
#['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# test total number of possible combinations
##print len(all_combinations(425)) == len(keypad['4']) * len(keypad['2']) * len(keypad['5'])