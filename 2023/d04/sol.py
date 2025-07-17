import os
import re
import pandas as pd

root = r'D:\OneDrive - Maxis Broadband Sdn Bhd\Desktop\advent-of-code\2023\d04'

with open(os.path.join(root, 'full.txt')) as f:
    lines = f.read()
lines = lines.split('\n')

sets = []
for card in lines:
    card2 = card.split(':')
    card3 = card2[1].split('|')
    win = set([int(z.strip()) for z in card3[0].split()])
    mine = set([int(z.strip()) for z in card3[1].split()])
    sets.append((win,mine))

win_val = []
for win, mine in sets:
    win_cards = win.intersection(mine)
    len_win = len(win_cards)
    if len_win in [0,1]:
        win_val.append(len_win)
    else:
        # power
        win_val.append(2**(len_win-1))
sum(win_val)

