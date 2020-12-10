# -*- coding: utf-8 -*-
"""
Day 4 puzzle

"""

import re

# import the input txt file
file1 = open('U:\\AdventOfCode_2020\\Day4_input.txt')
inputs = file1.read().split('\n\n')
inputs = list(filter(None, inputs))

# list all the valid fields required
valid = ['ecl','pid','eyr','hcl','byr','iyr','hgt']

# convert each entry into a dictionary
counter=0
for item in inputs:
    fields = dict([i.split(':') for i in item.replace('\n',' ').split(' ')])
    # Puzzle 1
    if len(set(valid).intersection(fields.keys()))==7:
        if int(fields.get('byr'))>=1920 and int(fields.get('byr'))<=2002:
            if int(fields.get('iyr'))>=2010 and int(fields.get('iyr'))<=2020:
                if int(fields.get('eyr'))>=2020 and int(fields.get('eyr'))<=2030:
                    if (re.search('\d{3}cm', fields.get('hgt')) and int(fields.get('hgt')[0:3])>=150 and 
                        int(fields.get('hgt')[0:3])<=193) or (re.search('\d{2}in', fields.get('hgt')) and 
                        int(fields.get('hgt')[0:2])>=59 and int(fields.get('hgt')[0:2])<=76):
                            if re.search('#\w{6}',fields.get('hcl')):
                                if fields.get('ecl') in ['amb','blu','brn','gry','grn','hzl','oth']:
                                    if len(fields.get('pid'))==9:
                                                counter+=1

print(counter)