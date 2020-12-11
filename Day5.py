# -*- coding: utf-8 -*-
"""
Day 5 puzzle

"""
import math
# import the input txt file
file1 = open('U:\\AdventOfCode_2020\\Day5_input.txt')
inputs = file1.read().split('\n')

# define functions to traverse seats
def get_row(sequence, front, back):
    if len(sequence)==1:
        return front if sequence[0]=='F' else back
    else:
        step = (back - front)/2
        return  get_row(sequence[1:], front, back - math.floor(step)-1) if sequence[0] == 'F' else get_row(sequence[1:],front+math.ceil(step), back)
    
def get_col(sequence, left, right):
    if len(sequence)==1:
        return left if sequence[0]=='L' else right
    else:
        step = (right - left)/2
        return  get_col(sequence[1:], left, right - math.floor(step)-1) if sequence[0] == 'L' else get_col(sequence[1:],left+math.ceil(step), right)
  

# initialize and run inputs    
ans=[]
for line in inputs:
    front, back = 0, 127
    left, right = 0, 7
    ans.append(get_row(line[:-3], front, back)*8 + get_col(line[-3:], left, right))
    
# Puzzle 1
print(max(ans))

# Puzzle 2
ans.sort()
i = 0
while ans[i+1]-ans[i]==1:
    i+=1
print(ans[i],ans[i+1])
