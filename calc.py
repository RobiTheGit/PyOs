import sys
import os
import subprocess

def math(): #define function math
    x = input("X=? ") #ask for user input for X
    math = input("Math Function(add, subtract, multiply, divide, power, root3, root2, x^y, y^x, convert)? ")#same but for math type
    if math == 'addition' or math == 'add' or math == '+': #does math equal adding?
        y = input("Y=? ") #ask for user input for  Y
        try: #if so try to run it
          print(f"{x} + {y} =", int(x) + int(y))# display to the user that x + y = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error
    elif math == 'subtraction' or math == "subtract" or math == '-': #does math equal subtracting?
        y = input("Y=? ") #ask for user input for  Y
        try: #if so try to run it
          print(f"{x} - {y} =", int(x) - int(y))# display to the user that x - y = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error
    elif math == 'multiplication' or math == "multiply" or math == '*': #does math equal multipling?
        y = input("Y=? ") #ask for user input for  Y
        try: #if so try to run it
          print(f"{x} * {y} =", int(x) * int(y))# display to the user that x * y = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error


    elif math == 'division' or math == 'divide' or math == '/': #does math equal dividing?
        y = input("Y=? ") #ask for user input for  Y
        try:
          print(f"{x} / {y} =", int(x) / int(y))# display to the user that x / y = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error

    elif math == 'power': #does math equal squaring?
        square = input(f"{x} to the power of ? ")
        try:
          print(f"{x}^{square} =", int(x) ** int(square))# display to the user that x^ power = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error

    elif math == 'x^y' or math == 'X^y' or math == 'x^Y' or math == 'X^Y': #does math equal squaring?
        y = input("Y=? ") #ask for user input for  Y
        try:
          print(f"{x}^{y} =", int(x) ** int(y))# display to the user that x^ power = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error

    elif math == 'y^x' or math == 'y^X' or math == 'Y^x' or math == 'Y^X': #does math equal squaring?
        y = input("Y=? ") #ask for user input for  Y
        try:
          print(f"{x}^{y} =", int(x) ** int(y))# display to the user that x^ power = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error

    elif math == 'root3': #does math equal roots?
        
        try:
          print(f"The cube root {x} =", int(x) ** .3333333333 )# display to the user that the cube root x  = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error

    elif math == 'root2': #does math equal roots?
        
        try:
          print(f"The square root {x} =", int(x) ** .5 )# display to the user that the square root x  = the answer to the equation
        except: #if errors, let them pass
          print("Error") #display that there was an error


    elif math == 'convert' or math == 'conversion': #does math equal convert?
        convert = input('Convert to US(cm to in) or Meteric(in to cm)? ')
        if convert == 'Metric':
          try:
             print(f"{x} in metric =", int(x) / 0.39370)# display to the user that x / 39.37 = the answer to the equation
          except: #if errors, let them pass
             print("Error") #display that there was an error
        if convert == 'Standard' or convert == 'US':
          try:
             print(f"{x} in standard =", int(x) * 0.39370)# display to the user that x * 39.37 = the answer to the equation
          except: #if errors, let them pass
             print("Error") #display that there was an error
             
             


    else:
        print("0 * 0 = 0")
   
    cont = input('Do you want to keep calculating? ')
    if cont == '1' or cont == 'y' or cont == 'yes':
        recurse() #run function recurse
    else:
        sys.exit(0)


def recurse(): #define function recurse
    math() #rerun function math
    recurse() #run function recurse to keep this going on forever

math()
