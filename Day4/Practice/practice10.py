#Date:4/07/2024
#Author:Aymen Sajjad

#Create a function that takes a numbr as input and prints its multiplication table


def multi_table(number):
    for i in range(1,11):
        result=i*number
        print(f"{number}X{i}={result}")


multi_table(9)        