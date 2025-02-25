"""
Author: Brian W
Date : 02/22/25
Description: Displays understanding of variable types and basic math operations
"""
import math
import time
Start= input("Start program? Yes/No ").lower()
#Asks user to start program and allows user to input Y/N
if Start=="yes":
 print("Beginning program...")
    #2 Second Delay
 time.sleep(2)
 #Splits code between type of variable printing and math operation calculator
 varORmath=input("Variables or Math? ").lower()
 #Split for variables
 if varORmath==("var" or "variable" or "variables"):
   #This is a float
   print("Float: ",float(1.1))
    #1 second delay to not overwhelm user
   time.sleep(1)
    #This is an integer
   print ("integer: ", int(1))
    #Another 1 second delay
   time.sleep(1)
    #This is a string
   print("String: str")
#Asks to print more bs
#Split for Math
 if varORmath==("math"):
   #prints bs and waits the piss people off
    print("Proceeding...")
    time.sleep(2)

    while True:
    #Input to begin operations
        Operation=input("What operation? Type list for list of operations. ")
   #new block for addition operation
        if Operation==("addition"):
    #asks for 2 numbers to add
            Add1=input("What is first number? ")
            Add2=input("What is second number? ")
   #Adds inputted numbers
            sum=float(Add1)+float(Add2)
   #Prints sum of numbers
            print("Sum is", sum)
   #new block for subtraction operation
        if Operation==("subtraction"):
      #asks for 2 numbers to subtracts
            Sub1=input("What is first number? ")
            Sub2=input("What is second number? ")
   #Applys subtraction
            difference=float(Sub1)-float(Sub2)
            print("difference is", difference)
   #new block for multiplication operation
        if Operation==("multiplication"):
      #asks for 2 numbers to multiply
            mult1=input("What is first number? ")
            mult2=input("What is the second number? ")
   #Applys operation
            product=float(mult1)*float(mult2)
   #prints products
            print("product is", product)
       #new block for division operation
        if Operation==("division"):
      #asks for 2 numbers to divide
            div1=input("What is first number? ")
            div2=input("What is second number? ")
   #Applys operation
            quotient=float(div1)/float(div2)
   #prints quotient
            print("quotient is", quotient)
   #new block for exponent
        if Operation==("exponent"):
      #asks for 2 numbers to exponentiate
            base=input("What is the base? ")
            exponent=input("What is the exponenet? ")
   #Applys operation
            power=float(base)**float(exponent)
   #prints power
            print("power is", power)
   
        if Operation==("list"):
            print("""addition
subtraction
multiplication
division
exponent
root
       """)
            repeatoperation=input("Input operation to continue. ").lower()
            if repeatoperation==("operation"):
                break