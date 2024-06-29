#Date:29/6/2024
#Author:Aymen Sajjad


# wrtie a program thst calculate a factorial of a given number

#using built in function


from math import factorial
def fact_num(number):
    return factorial(number)

print(fact_num(9))



#manually finding factorial

def fact_num(number):
    product=1
    for i in range(1,number+1):
        product*=i
    return product
    

print(fact_num(5))

#recursion method

def factorial_fun(n):
    if n <1:
        return None
    for i in range(1,n+1):
     if n==1:
         return 1
    return n * factorial_fun(n-1)



