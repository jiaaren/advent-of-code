import os
import re
import pandas as pd

root = r'D:\OneDrive - Maxis Broadband Sdn Bhd\Desktop\advent-of-code\2023\d03'

with open(os.path.join(root, 'full.txt')) as f:
    lines = f.read()
lines = lines.split('\n')
grid = [list(l) for l in lines]
lines[0]
matches = [list(re.finditer('[0-9]+',l)) for l in lines]
# create data structure
matches_lst = []
for row_i, match_lst in enumerate(matches):
    for match in match_lst:
        # matches_dict[(row_i,match.start())] = int(match.group())
        matches_lst.append((row_i, match.start(), int(match.group())))
        # span = match.span()
        # match.group()
        # match.start()

nrow = len(grid)
ncol = len(grid[0])

# Q1
def isin_bounds(row_idx, col_idx):
    if row_idx < 0 or col_idx < 0 \
        or row_idx >= nrow or col_idx >= ncol:
        return False
    return True

def get_coords(row_idx, col_idx, num):
    ndigit = len(str(num))
    coords = [(row_idx, col_idx-1), (row_idx, col_idx+ndigit)]
    for j in range(col_idx-1, col_idx+ndigit+1):
        coords.extend([(row_idx-1,j), (row_idx+1,j)])
    return coords

def check_symbol_adjacent(row_idx, col_idx, num):
    coords = get_coords(row_idx, col_idx, num)
    for y, x in coords:
        if isin_bounds(y, x) and not grid[y][x].isdigit() and grid[y][x] != '.':
            return True
    return False

# Q1
df = pd.DataFrame(matches_lst)
df.columns = ['y','x','val']
df['symbol'] = df.apply(lambda row: check_symbol_adjacent(row.y, row.x, row.val), axis=1)
sum(df.loc[df['symbol'],'val'])

# Q2
## Process coords
matches_dict = {}
for y,x,val in matches_lst:
    coords = [z for z in get_coords(y,x,val) if isin_bounds(z[0],z[1])]
    matches_dict[(y,x)] = coords

df2 = pd.DataFrame(data={'point_coor':matches_dict.keys(),'coords':matches_dict.values()})
df2 = df2.explode('coords').reset_index(drop=True)
def get_val(y2,x2):
    for y,x,val in matches_lst:
        if y2 == y and x2 == x:
            return val

df2['val'] = df2['point_coor'].apply(lambda z: get_val(z[0],z[1]))
del df2['point_coor']
coord_count = df2.groupby('coords').count()
merged = df2.merge(coord_count, right_index=True, left_on='coords')
merged.columns = ['coords','val','count']
merged['char'] = merged['coords'].apply(lambda z: grid[z[0]][z[1]])

df3 = merged.loc[(merged['char'] == '*') & (merged['count'] == 2),:]
prods = df3.groupby('coords')['val'].prod()
prods
# 80403602
sum(prods)



