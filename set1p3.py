#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:48:42 2018

@author: jd
"""
s = 'ovjvnpklq'
longestLength = 0
longest = ''
index = 0
for index in range(len(s)):
    long  = ''
    for n in range(len(s) - index):
        if n == 0:
            long = s[index]
            if index == 0 and longestLength == 0:
                longest = long
        elif long[len(long) - 1] <= s[index + n]:
            long = long + s[index + n]
            if len(long) > longestLength:
                longest = long
                longestLength = len(longest)
        else:
            break
print('Longest substring in alphabetical order is: ' + longest)
            