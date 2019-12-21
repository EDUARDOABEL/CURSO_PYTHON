# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:28:20 2019

@author: CEC
"""

    


file=open("devices.txt","a")
while True:
    newItem = input("Ingrese un nuevo item: ")
    if newItem == 'exit':
        print("todo Listo!!")
        break
    else:
        file.write(newItem + "\n") 

file.close()