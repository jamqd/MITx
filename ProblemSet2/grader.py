#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:31:46 2018

@author: jd
"""

import math

"""
Function returns sum of area and square of perimeter of n-sided regular polygon
Parameters
    n - number of sides
    s - side length
Return
    sum of area and square of perimeter of n-sided regular polygon rounded to 4 decimal places    
"""

def polysum(n, s):
    #calculate area
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    
    #calculate perimeter
    perimeter = n * s
    
    #calculate return value
    total = area + perimeter ** 2
    
    #return and round return value
    return round(total, 4)