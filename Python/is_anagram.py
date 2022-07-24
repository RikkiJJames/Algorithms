# -*- coding: utf-8 -*-

from collections import Counter

#Leetcode 242
def is_anagram(string1, string2):
    
    if len(string1) != len(string2):
        return False
    
    a = Counter(string1)
    b = Counter(string2)
    
    if a == b:
        return True
    else:
        return False
    
    
s = "anagram"
t = "nagaram"

strings = [("anagram", "nagaram" ), ("rat", "car")]

for s, t in strings:
    print(is_anagram(s,t))
