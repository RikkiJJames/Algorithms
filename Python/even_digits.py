# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:24:32 2022

@author: Rjjam
"""

#leetcode 1295
import math

def even_digits(nums):
    
    even = 0
    
    for x in nums:
        if int(math.log10(x) + 1) % 2 == 0:
            even += 1
    
    return even

data = [12, 345, 2, 6, 7896]

print(even_digits(data))