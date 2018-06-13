#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:40:22 2018

@author: jd
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0
monthlyUnpaidBalance = balance


for n in range (1,13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    #print('Month ' + str(n) + ' Remaining balance: ' + str(round(balance, 2)))
print('Remaining balance: ' + str(round(balance, 2)))