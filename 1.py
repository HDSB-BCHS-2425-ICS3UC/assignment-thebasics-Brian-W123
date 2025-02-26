"""
Author: Brian W
Date : 02/22/25
Description: Displays understanding of variable types and basic math operations
"""
import math
import time
while True:
     Start= input("Start program? Yes/No ").lower()
     #Asks user to start program and allows user to input Y/N
     if Start=="yes" or Start=="y" or Start=="five guys burgers and fries":
          print("Beginning program...")
          #2 Second Delay
          time.sleep(2)
          #Splits code between type of variable printing, math operation calculator or 3D volume
          varORmath=input("""
     Variables Demonstration, 
     Simple Calculator,
     or
     3D volume calculator? """).lower()
          #Split for variables
          if varORmath=="var" or varORmath=="variable" or varORmath=="variables" or varORmath=="variables demonstration":
               #This is a float
               print("This is a float: ",float(1.1))
               #1 second delay to not overwhelm user
               time.sleep(1)
               #This is an integer
               print ("this is an integer: ", int(1))
               #Another 1 second delay
               time.sleep(1)
               #This is a string
               print("This is a string: String")
               #Breaks loop
               break
               #Split for Math
          if varORmath=="math" or varORmath=="calculator" or varORmath=="simple calculator" or varORmath=="math calculator":
               #prints bs and waits the piss people off
               print("Proceeding...")
               time.sleep(2)
               #while loop to reset code if list is selected as an option
               while True:
                    #Input to begin operations
                    Operation=input("What operation? Type list for list of operations. ")
                    #new block for addition operation
                    if Operation==("addition" or Operation=='add'):
          #asks for 2 numbers to add
                         Add1=input("What is first number? ")
                         Add2=input("What is second number? ")
                         #Adds inputted numbers
                         sum=float(Add1)+float(Add2)
                         #Prints sum of numbers
                         print("Sum is", sum)
                         break
                    #new block for subtraction operation
                    if Operation=="subtraction" or Operation=='sub':
                         #asks for 2 numbers to subtracts
                         Sub1=input("What is first number? ")
                         Sub2=input("What is second number? ")
                         #Applys subtraction
                         difference=float(Sub1)-float(Sub2)
                         print("difference is", difference)
                         break
                         break
                    #new block for multiplication operation
                    if Operation=="multiplication" or Operation=="mult":
                         #asks for 2 numbers to multiply
                         mult1=input("What is first number? ")
                         mult2=input("What is the second number? ")
                         #Applys operation
                         product=float(mult1)*float(mult2)
                         #prints products
                         print("product is", product)
                         break
                    #new block for division operation
                    if Operation=="division" or Operation=="div":
                         #asks for 2 numbers to divide
                         div1=input("What is first number? ")
                         div2=input("What is second number? ")
                         #Applys operation
                         quotient=float(div1)/float(div2)
                         #prints quotient
                         print("quotient is", quotient)
                         break
                    #new block for exponent
                    if Operation=="exponent" or Operation=="exp":
                         #asks for 2 numbers to exponentiate
                         base=input("What is the base? ")
                         exponent=input("What is the exponent? ")
                         #Applys operation
                         power=float(base)**float(exponent)
                         #prints power
                         print("power is", power)
                         break
                    #new block for sqrt
                    if Operation=="square root" or Operation=='root':
                         #asks for 1 number to sqrt
                         sqrt=input("What is the number? ")
                         #Applys operation
                         sqrted=math.sqrt(float(sqrt))
                         #prints product
                         print("product is", sqrted)
                         break
                    #new block for discriminant
                    if Operation=="discriminant" or Operation=='dis':
                         #asks for a, b, and c
                         discriminantA=input("What is the 'a' value? ")
                         discriminantB=input("What is the 'b' value? ")
                         discriminantC=input("What is the 'c' value? ")
                         #Applys operation
                         discriminantoutput=float(discriminantB)**2-4*float(discriminantA)*float(discriminantC)
                         #prints product
                         print("discriminant is", discriminantoutput)
                         break



                    #if list is inputed this if statement will print available operations and repeat loop
                    if Operation==("list"):
                         print("""addition
subtraction
multiplication
division
exponent
square root
discriminant
     """)
                         False
                    
                    #else statement to break the loop
                    else:
                         print("No valid input recognised, run code again")
                         break
                         break

          #while loop to repeat from list in volume branch
          while True:
               #branch for volume calculation
               if varORmath=="3d calculator" or varORmath=='3d' or varORmath=='volume':
                    #gotta print some bs and make the user wait to make bug testing annoying
                    print("proceeding...")
                    time.sleep(1)
                    #input to branch into all shapes
                    shape=input("Which shape? Input list for shape. ").lower()
                    #if list is inputed this will list available shapes and loops to top
                    if shape=="list":
                         print("""cube
sphere
cone
cylinder
     """)
                         False
                    #else statement to break loop really fast
                    else:
                         print("No valid input recognised, run code again")
                         break
                         break

     
     else:
          print("""Try Again
          """)
          False