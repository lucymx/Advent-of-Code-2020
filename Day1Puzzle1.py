# -*- coding: utf-8 -*-
"""
Day 1 Puzzle

"""

import numpy as np

# import the input txt file
file1 = open('U:\\AdventOfCode_2020\\Day1Puzzle1_input.txt')
input_txt = file1.read().split('\n')
inputs = [int(i) for i in input_txt]
# inputs = [1721,979,366,299,675,1456]

# initialize answer
ans = []


# sum every possible pair in the list. if it equals 2020, store in new list
for i in range(len(inputs)-2):
    for j in range(i+1,len(inputs)-1):
        for k in range (j+1,len(inputs)):
            if inputs[i]+inputs[j]+inputs[k] == 2020:
                ans.extend([inputs[i],inputs[j],inputs[k]])
print(np.prod(ans))