#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:48:42 2018

@author: jd
"""
s = 'hnggudhhgr'
longestLength = 0
longest = ''
index = 0
for index in range(len(s)):
    print(str(index))
    for n in range(index, len(s) -2):
        if s[index + n] <= s[index + n + 1]:
            if longestLength < int(len(s[index-1:index + n])):
                print(s[index - 1:index + n])
                longestLength = len(s[index - 1:index + n])
                print(str(longestLength))
                longest = s[index -1:index + n]
print('Longest substring in alphabetical order is: ' + longest)
            