import os

root = r'D:\OneDrive - Maxis Broadband Sdn Bhd\Desktop\advent-of-code\2023\d03'

with open(os.path.join(root, 'example1.txt')) as f:
    lines = f.read()
lines = lines.split('\n')
grid = [list(l) for l in lines]
nrow = len(grid)
ncol = len(grid[0])

# Q1
coords = [(-1,-1),(-1,0),()]
def check_symbol_adjacent(row_idx, col_idx):
    return
