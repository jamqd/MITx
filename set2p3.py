#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:12:50 2018

@author: jd
"""

balance = 320000
annualInterestRate = 0.2

monthlyRate = annualInterestRate/12.0
lower = balance / 12
upper = (balance * (1 + monthlyRate) ** 12) / 12.0
error = 0.01

zBalance = balance
monthlyPayment = 0

while abs(zBalance) > error:
    zBalance = balance
    monthlyPayment = lower + (upper - lower )/2
    for n in range(1,13):
        zBalance -= monthlyPayment
        zBalance += monthlyRate * zBalance
    if zBalance > 0:
        lower = monthlyPayment
    else:
        upper = monthlyPayment
print('Lowest Payment: ' + str(round(monthlyPayment, 2)))