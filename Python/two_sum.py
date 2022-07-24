# -*- coding: utf-8 -*-

# leetcode 1

nums = [2,7,11,15]
target = 9

def two_sum(nums):
    
    dict1 = {}
    
    for index, x in enumerate(nums):
        difference = target - x
        if difference in dict1:
            return [dict1[difference], index]
        dict1[x] = index
    

    