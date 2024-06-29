#Dated:27/6/2024
#Author:Aymen Sajjad

#Implement a program that find a largest number in a string

lst_number=[1,3,5,7,9,5,10]
largest_number=0
for i in lst_number:
    if i > largest_number:
        largest_number=i

print(largest_number)

#using built in function
lst_number=[1,3,5,7,9,5,10]
print(max(lst_number))