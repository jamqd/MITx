#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:04:31 2018

@author: jd
"""

s = 'azcbobobegghakl'
count = 0
for letter in s:
    if letter  == 'a' or letter  == 'e' or letter  == 'i' or letter  == 'o' or letter  == 'u':
        count += 1
print('Number of vowels: ' + str(count))