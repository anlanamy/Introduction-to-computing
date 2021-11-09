#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:56:19 2020

@author: anlanamy
"""

#10 beautiful matrix
for i in range(5):
    l=input().split()
    for j in range(5):
        if l[j]=='1':
            print(abs(i-2)+abs(j-2))
            break