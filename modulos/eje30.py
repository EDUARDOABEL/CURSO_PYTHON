# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:46:34 2019

@author: CEC
"""


def fib(n):
    a, b = 0,1
    while a < n:
        print(a,end=" ")
        """ c=a+b
        a=b
        b=c"""
        a,b=b, a+b 
    print()
   