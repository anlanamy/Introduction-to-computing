#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:10:35 2021

@author: anlanamy
"""
n=int(input())
maps=[]
for i in range(n):
    maps.append(list(input()))
for i in range(n):
    for j in range(n):
        print(i,j,maps[i][j])
        if maps[i][j]=='1':
            break