#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:59:49 2019

@author: diego
"""

list = [1,2,3,4,5,6,7,8,9,10]
i=0
while i < len(list):
    cuantas = 0
    while cuantas < list[i]:
        print(list[i])
        cuantas +=1
    i += 1    
       