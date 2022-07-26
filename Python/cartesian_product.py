# -*- coding: utf-8 -*-
'''
computers cartesian product of input iterables
print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
'''

from itertools import product


def cartesian_product(a, b):
    a = list(map(int, a))
    
    b = list(map(int, b))
    
    
    return product(a,b)

a = [1, 2]
b = [3, 4]

print(*cartesian_product(a,b))


