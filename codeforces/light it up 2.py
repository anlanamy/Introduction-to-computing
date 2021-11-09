#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:46:35 2020

@author: anlanamy
"""

n,m=map(int,input().split())
l=[0]+[int(x) for x in input().split()]+[m]
b=[0]*(n+1)
b[0]=l[1]-l[0]
for i in range(1,n+1):
    b[i]=b[i-1]+(l[i+1]-l[i])*((i+1)%2)
a=b[-1]
for i in range(1,n+1,2):
    if l[i+1]-l[i]>1:
        a=max(a,b[i-1]+m-b[-1]-l[i]+b[i-1]-1)
print(a)