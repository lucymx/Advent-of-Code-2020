# -*- coding: utf-8 -*-
"""
Day 2 Puzzle

"""

# import the input txt file
file1 = open('U:\\AdventOfCode_2020\\Day2_input.txt')
inputs = file1.read().split('\n')
#inputs = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']

# define functions to parse and validate each password
def parse(input_str):
    # get the key character, range, and password into separate variables
    rng = [int(i) for i in input_str.split()[0].split('-')]
    key = input_str.split()[1][0]
    pw = input_str.split()[2]
    return rng, key, pw

# Puzzle 1
def validate(rng, key, pw):  
    #now check the password for number of occurrences of the key
    keycount = pw.count(key)
    #if the count is within the range, return true else false
    if keycount >= rng[0] and keycount <= rng[1]:
        return True
    else:
        return False

# Puzzle 2
def validate_pos(rng, key, pw):
    # now we need to ensure the key occurs in one of the two positions in the range
    # intitialize the counter
    counter = 0    
    for pos in rng:
        if pw[pos-1] == key:
            counter+=1
    if counter == 1:
        return True
    else:
        return False
    
# initialize answer
ans1 = []
ans2 = []
# check every string in the inputs list
for string in inputs:
    rng, key, pw = parse(string)
    ans1.append(validate(rng, key, pw))
    ans2.append(validate_pos(rng, key, pw))
    
print(sum(ans1))
print(sum(ans2))

