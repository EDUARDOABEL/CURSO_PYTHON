# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:23:03 2019

@author: CEC
"""
while True:
    edad=int(input ("cual es tu edad : "))
    if edad <=20:
      print("ERES JOVEN")
    elif edad >=21 and edad <= 50:
        print("eres adulto")
    elif edad == "q" or edad == "quit":
        break
    else:
        print("ya estas viejo")
      
     