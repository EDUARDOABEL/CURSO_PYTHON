# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:01:50 2019

@author: CEC
"""

while True:
    firstname = input("Cuál es su primer nombre? ")
    lastname = input("Cuál es su apellido? ")
    location = input("Cuál es su dirección? ")
    age = input("Cuál es su edad? ")
    x=int(age)
    space = " "
    print("Hola" + space + firstname + space + lastname + ", tienes" + space + age + space + "años y vives en" + space + location)
    if x > 1 and x <= 12:
        print("*** Usted es un niño")
    elif x > 12 and x <= 18:
        print("*** Usted es un adolescente")
    elif x > 18 and x <= 65:
        print("*** Usted es un adulto")
    else:
        print("*** Usted es un adulto mayor")
    salir = input("Desea salir? [S] o [N] ")
    if salir == 'S':
        break
print ("Gracias")