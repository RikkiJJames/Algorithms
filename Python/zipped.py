# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:17:03 2022

@author: Rjjam
"""
#hackerank Zipped!


number_of_students, number_of_scores = map(int, input().split())

score_sheet = []

for _ in range(number_of_scores):
    score_sheet.append ( map(float, input().split()) )
    


for i in zip(*score_sheet):
    print(sum(i)/ number_of_scores)

    



