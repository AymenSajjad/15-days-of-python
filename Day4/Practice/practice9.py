#Date:4/07/2024
#Author:Aymen Sajjad

#Implement a function to check if a given year is leap year or not.


def leap_year(year):
    if year<1580:
        return f"{year}not in the era"
    if  (year%100==0)and(year%400==0)or(year%4==0)and(year%100!=0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
    

print(leap_year(2000) )   