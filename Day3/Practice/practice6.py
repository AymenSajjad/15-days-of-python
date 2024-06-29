#Date:29/6/2024
#Author:Aymen Sajjad


#implement a program that print multiplication table of given number



def mul_table(num):
    for i in range (1,10):
        result=i*num
        print(f"{num}X{i}={result}")
           


mul_table(4)