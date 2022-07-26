# -*- coding: utf-8 -*-
"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""
#leetcode 1342

def number_of_steps(num):
        
    operations = 0
        
    while (num != 0):
        if num % 2 != 0:
            operations += 1
            num -= 1
        else:
            operations += 1
            num /= 2

    return operations
    
    

print(number_of_steps(14))