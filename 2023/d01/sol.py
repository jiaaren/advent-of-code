import re

with open('1text2.txt') as f:
    file = f.read()

# problem 1
lines = file.split("\n")
lines_upt = [re.sub('[^0-9]', '', x) for x in lines]
values = [int(f'{s[0]}{s[-1]}') for s in lines_upt]
sum(values)

# problem 1
num_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('2text.txt') as f:
    file = f.read()

# problem 1
lines = file.split("\n")
def replace_num(s):
    for key, val in num_dict.items():
        s = s.replace(key, val)
    return s
lines_upt = [replace_num(s) for s in lines]

