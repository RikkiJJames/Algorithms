# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:13:45 2022

@author: Rjjam
"""
#Leetcode 347
from collections import Counter

def top_k_frequent(nums, k):
    
    counter = Counter(nums)
    
    counter = counter.most_common(k)
    
 
    return [values[0] for values in counter]

nums = [[1,1,1,2,2,3],[1]]
k = [2,1]

for x in range(len(nums)):
    print(top_k_frequent(nums[x], k[x]))

    