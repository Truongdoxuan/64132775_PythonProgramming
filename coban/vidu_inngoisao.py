# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 10:58:39 2025

@author: dxt81
"""
n = int(input())
print("Hình 1")
print((('*'*n)+'\n')*n)

print("Hình 2")
for i in range(1,n+1):
    print('*'*i)