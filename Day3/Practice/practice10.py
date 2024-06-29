#Date:29/6/2024
#Author:Aymen Sajjad

#Calculate the sum of digit of a given number

#using built in function sum
def add_number(number):
    Sum=0
    for i in number:
        i=int(i)
        Sum+=i
    return Sum


print(add_number("457"))

