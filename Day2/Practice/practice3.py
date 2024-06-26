#Date:26/06/2024
#author:Aymen Sajjad


#Implemetn a program that checks if a given string is palindrome

str=input("Enter a string")
str_reverse="".join(reversed(str))

if str==str_reverse:
    print("the string is palindrome")
else:
    print("The string is not a palindrome")





 #another method

def reverse_string(str_1):
   reverse_str = ""
   for i in str_1:
      reverse_str = i + reverse_str    #reverse a string 
   if str_1==reverse_str:
      return "the string is palindrome"
   else:
      return "The string not a palindrome"
 
str_input = input("Enter a string")
reversing=reverse_string(str_input)    #function call
print(reversing)