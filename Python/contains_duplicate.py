# -*- coding: utf-8 -*-



#Leetcode 217

def contains_duplicate(nums):
    
    s = set()
    
    for value in nums:
        
        if value in s:
            return True
        else:
            s.add(value)
            
    return False
            

nums = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3], [0, 0], [0], [-1, -2 ,0 ,-5, 4]]

for x in nums:
    print(contains_duplicate(x))