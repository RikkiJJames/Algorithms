# -*- coding: utf-8 -*-
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

# leetcode 9 

def palindrome_number(x):
        """
        :type x: int
        :rtype: bool
        """
        
        str_x = str(x)
        
        rev_x = str_x[::-1]
        
        if str_x == rev_x:
            return True
        else:
            return False
        
        
nums = [121, -121, 10, 23232]

for x in nums:
    print(palindrome_number(x))