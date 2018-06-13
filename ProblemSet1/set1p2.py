#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:04:50 2018

@author: jd
"""

s = 'azcbobobegghakl'
first = ''
second = ''
third = ''
count = 0
for letter in s:
    first = second
    second = third
    third = letter
    if (first + second + third) == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))