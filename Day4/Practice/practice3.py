#Date:4/07/2024
#Author:Aymen Sajjad

#Write a function  that returns the factorial of a given number using recursion

def factorial_fun(n):
    if n <1:
        return None
    for i in range(1,n+1):
     if n==1:
         return 1
    return n * factorial_fun(n-1)

print(factorial_fun(9))


#using built in function
from math import factorial

def factorial_fun(n):
    number=factorial(n)
    return number

print(factorial_fun(9))
