import os
import re
import pandas as pd

root = r'D:\OneDrive - Maxis Broadband Sdn Bhd\Desktop\advent-of-code\2023\d02'

with open(os.path.join(root, 'full.txt')) as f:
    lines = f.read()
lines = lines.split('\n')

# Q1
games_dict = {}

for game in lines:
    game_split = game.split(':')
    game_idx = int(game_split[0].strip('Game '))
    sub_games = game_split[1].split(';')
    sg_dict = {}
    for i, sg in enumerate(sub_games):
        sg = [tuple(s.strip().split()) for s in sg.split(',')]
        sg_dict[i] = {col:int(num) for num,col in sg}
    games_dict[game_idx] = sg_dict

def getmax(games_dict_item):
    tmp_df = pd.DataFrame(games_dict_item.values()).fillna(0)
    return tmp_df.apply(max, 0).to_dict()

max_df = pd.DataFrame([getmax(x) for x in games_dict.values()])
max_df.index = games_dict.keys()
bool_q1 = (max_df['red'] <= 12) & (max_df['green'] <= 13) & (max_df['blue'] <= 14)
sum(max_df.index[bool_q1])

# Q2
sum(max_df.red * max_df.blue * max_df.green)
