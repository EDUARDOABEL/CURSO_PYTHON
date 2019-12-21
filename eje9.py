# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:58:07 2019

@author: CEC
"""

while True:
    x=input("Cuantas veses quiere contar :")
    if x == "q" or x == "quit":
        break
    x= int (x)
    y=1
    while True:
        print (y)
        y=y+1
        if y>x:
            break