# -*- coding: utf-8 -*-
"""
Day 3

"""

import numpy as np
import pandas as pd

# import the input txt file
file1 = open('U:\\AdventOfCode_2020\\Day3_input.txt')
inputs = file1.read().split('\n')
df = pd.DataFrame([list(row) for row in inputs])

# get the length of a single row. this will help determine which position to loop to when it goes out of bounds
length = len(df.columns)

# define functions find the next position and check whether there's a tree
def next_step(start_col, start_row, right_step, down_step):
    end_row = start_row + down_step
    if start_col + right_step > length - 1:
    # divide the i position by loop length. the remainder is the reduced column
        end_col = (start_col + right_step)%length
    else:
        end_col = start_col + right_step
    return end_row, end_col

def check_tree(char):
    if char == '#':
        return True
    else:
        return False
    
# puzzle 2 new function to traverse the full map on given step size
def traverse(df, right_step, down_step):
    row, col = 0, 0
    step_ans = []
    while row < len(df):
        step_ans.append(check_tree(df.loc[row,col]))
        row, col = next_step(col, row, right_step, down_step)
    return sum(step_ans)
    
ans = []
step_inputs = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for step in step_inputs:
    ans.append(traverse(df, step[0], step[1]))
    
print(ans)
print(np.product(ans))
ans = np.array(ans, dtype = np.float64)
print(np.product(ans))