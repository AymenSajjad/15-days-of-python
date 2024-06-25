#Date:25/6/2024
#Author:Aymen Sajjad

#Create a python function to check if a given string is Palindrome

def reversefunction(str): #function definition
    
    reverse_str="".join(reversed(str)) #used builtin reverse function
    if str==reverse_str: #check if two string or equal or not
        print("Number is Palindrome")
    else:
        print("it is not a palindrome")
     
reversefunction("apple") #function call
reversefunction("atta") #function call





#using structural programing
str=input("Enter a string to check")
reversestr="".join(reversed(str))
print(reversestr)
if str==reversestr:
    print("Number is Palindrome")
else:
    print("it integer Number")
    