# -*- coding: utf-8 -*-
"""
Day 6 puzzle

"""
# import the input txt file
file1 = open('U:\\AdventOfCode_2020\\Day6_input.txt')
inputs = file1.read().split('\n\n')

ans = []
for item in inputs:
    count=0
    entries = item.split('\n')
    for letter in set(''.join(entries)):
        if len([letter for i in entries if letter in i])==len(entries):
            count+=1
    ans.append(count)
print(sum(ans))
    
