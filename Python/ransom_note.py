# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:49:03 2022

@author: Rjjam
"""
#leetcode 383
from collections import Counter

def ransom_note(note, magazine):
        
        m = Counter(magazine)
        r = Counter(note)
        
        intersect = m & r
        
        if intersect == r:
            return True
        else: 
            return False
        
    
note = "aaac"
magazine = "abaac"

print(ransom_note(note, magazine))
        