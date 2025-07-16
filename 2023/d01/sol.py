import re
import os

root = r'D:\OneDrive - Maxis Broadband Sdn Bhd\Desktop\advent-of-code\2023\d01'
with open(os.path.join(root,'full.txt')) as f:
    file = f.read()

# problem 1
lines = file.split("\n")
lines_upt = [re.sub('[^0-9]', '', x) for x in lines]
values = [int(f'{s[0]}{s[-1]}') for s in lines_upt]
sum(values)


# problem 2
num_dict = {
    # 'zero': '0',
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

num_dict_rev = {k[::-1]:v for k,v in num_dict.items()}


with open(os.path.join(root, 'full.txt')) as f:
    file = f.read()
lines = file.split("\n")

# problem 2
s = 'eightwothree'

def replace_(s, num_dict):
    found_lst = []
    for k,_ in num_dict.items():
        iter_ = re.finditer(k, s)
        item = next(iter_, 'na')
        if item != 'na':
            found_lst.append((k, item.span()[0]))
    if found_lst:
        found_lst.sort(key=lambda x: x[1])
        upt_key = found_lst[0][0]
        # e.g. s.replace('eight', '8', 1)
        return s.replace(upt_key, num_dict[upt_key], 1)
    else: return s

def func(s):
    new_s = s
    while(True):
        new_s = replace_(new_s, num_dict)
        if new_s == s: break
        s = new_s
    # s = replace_(s, num_dict)
    # s = replace_(s[::-1], num_dict_rev)[::-1]
    return s

lines_upt = [func(s) for s in lines]
lines_upt = [re.sub('[^1-9]', '', x) for x in lines_upt]
values = [int(f'{s[0]}{s[-1]}') if len(s) > 1 else int(s[0]) for s in lines_upt]
# values = [int(f'{s[0]}{s[-1]}') for s in lines_upt]
sum(values)


f('fiveqpstwo4rnxd75fjgpv')