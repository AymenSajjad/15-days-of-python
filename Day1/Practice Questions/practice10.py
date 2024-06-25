#Date:25/6/2024
#Author:Aymen Sajjad


#implement a program the swapp the values of two 

def Swap_value(x,y):
    temp=x  #make a Temporory variable to store a value through which swapping occurs
    x=y     #x has now 23
    y=temp  #y has value of temp which is 20
    print("the values after swapping is:",x,y)

Swap_value(x=20,y=23) #function call