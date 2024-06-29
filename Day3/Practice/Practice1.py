#Date:29/6/2024
#Author:Aymen Sajjad

#Create a program that takes a year as input and check if its leap year or not

year=int(input("Enter a year"))

if year<1580:
    print("not in the era")
elif (year%100==0) and (year%400==0) or (year%4==0) and (year%100!=0):
    print("its a leap year") 
else:
    print("its not a leap year")       