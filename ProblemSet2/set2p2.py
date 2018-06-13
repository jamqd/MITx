#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:14:37 2018

@author: jd
"""
balance = 3926
annualInterestRate = 0.2

monthlyRate = annualInterestRate/12.0
monthlyPayment = round(monthlyRate * balance, -1)

zBalance = balance
while zBalance > 0:
    for n in range (1,13):
        zBalance -= monthlyPayment
        zBalance += monthlyRate * zBalance
    if zBalance > 0:
        monthlyPayment += 10
        zBalance = balance
print('Lowest Payment: ' + str(monthlyPayment))