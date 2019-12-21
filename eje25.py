# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:41:00 2019

@author: CEC
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
 

#numeros primos

numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
     if numero % n == 0:
        contador +=1
        print("divisor:", n)
     if contador > 0 :
        print("El número no es primo" )
     else:
        print("El nÚmero es primo")


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(isPrime(7))
    
#años bisiestos

anio = int(input("Ingresa el año : "))
if  anio %4==0  and anio %100 !=0 or anio % 400==0 :
 print( "Es bisiesto")
else:
 print( "No es bisiesto")
 
def isYearLeap(year):
     if year % 4 !=0:
         return False
     elif year % 100 !=0:
         return True
     elif year % 400 !=0:
         return False
     else:
         return True
     
print(isYearLeap(2019))

#poner el año y saver cuantos dias tiene el mes

anio = int(input("Ingresa el año : "))
mes= int(input("Ingresa el numero de mes : "))

if  anio %4==0  and anio %100 !=0 or anio % 400==0 :
    mes2=[31,29,31,30,31,30,31,31,30,31,30,31]
    
    print( "Es bisiesto")
    print( "el mes tiene" , mes2[mes-1])
else:
    mes2=[31,28,31,30,31,30,31,31,30,31,30,31]
    print( "No es bisiesto")
    print( "el mes tiene" , mes2[mes-1])


# otra manera


def isYearLeap(year):
    if(year%4 == 0 and year%100 !=0 or year%400==0):
        return True
    return False

def daysInMonth(year, month):
    meses = [2,4,6,9,11]
    if month not in meses:
        return 31
    elif(isYearLeap(year) and month ==2):
        return 29
    elif month==2:
        return 28
    else:
        return 30

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")

#ejercicio año mes dia
    
def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if year < 1500 or month < 1 or month >12:
        return None
    days=[31,28,30,31,30,31,30,31,30,31,30,31]
    res = days[month-1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res

def dayOfYear(year, month, day):
    
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2000, 12, 10))












    
     
