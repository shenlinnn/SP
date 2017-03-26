import collections
from config import keypad

def count_key_press(input):
    char_count_dict = collections.Counter(input)
    char_count = sorted(char_count_dict.items())
    n_press = 0
    for char_pair in char_count:
        char = char_pair[0]
        count = char_pair[1]
        for key, value in keypad.iteritems():
            if char in value:
                index = value.index(char) + 1
                break
        n_press += index * count
    return n_press

print count_key_press('hello')
#13
print count_key_press('wonderful')
#20

def number_pressed(input):
    key_pressed = ''
    for char in input:
        for key, value in keypad.iteritems():
            if char in value:
                key_pressed += key
                break
    return int(key_pressed)

print number_pressed('hello')
#43556
print number_pressed('wonderful')
#966337385