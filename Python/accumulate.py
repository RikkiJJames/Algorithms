# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:14:25 2022

@author: Rjjam
"""
from itertools import accumulate
import operator

def add(a, b):
    
    return a + b

def multiply(a, b):
     
    return a * b

def running_total(nums):

    
    l = list(accumulate(nums, operator.mul))
    
    print(l)
    
    

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


running_total(data)
    