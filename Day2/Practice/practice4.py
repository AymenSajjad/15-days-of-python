#Date:26/6/2024
#Author:Aymen Sajjad

#create a function to reverse a given string

def reverse_string(str_1):  #function definition
     reverse_str = ""

     for i in str_1:
        reverse_str = i + reverse_str  #reverse a string
     return reverse_str
 
str_input = input("Enter a string")
print(reverse_string(str_input))  #function call



#using built in function

str=input("Enter a string")
str_reverse="".join(reversed(str))
print("the reverse string is : ",str_reverse)