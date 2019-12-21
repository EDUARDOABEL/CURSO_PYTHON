# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:14:09 2019

@author: CEC
"""

try:
    x=int(input("enter a number: "))
    y=1/x
    print(y)
except zeroDivisionError:
    print("you cannot divide by zero, sorry.")
except valueError:
    print(" ojo")    
     
    
try:
    y=1/0
except ZeroDivisionError:
    print("Zero Division")
except ArithmeticError:
    print("Arit problem!!")
    print ("then end")
    
        
    def badFun(n):
        return 1/n
    try:
        badFun(0)
    except ArithmeticError:
        print("What happened ? An exception was raised !.")
    print("Then End")   



  

def validarNumero(prompt, min, max):
    while (True):
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Wrong input")
        except:
            print("The value is not within permitted range (-10..10)")
    
v = validarNumero("Enter a number from -10 to 10:", -10, 10)

print("The number is:", v)






