# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:20:21 2022

@author: Rjjam
"""
#leetcode 485
def max_consecutive_ones(nums):
        
        maximum_count  = 0
        temp_count = 0
        
        for x in nums:
            if x == 1:
                temp_count += 1
                if temp_count > maximum_count:
                    maximum_count = temp_count
            else:
                temp_count = 0
        
        return maximum_count
    
x = [1,1,0,1,1,1]
print(max_consecutive_ones(x))