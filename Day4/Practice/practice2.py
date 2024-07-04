#Date:4/07/2024
#Author:Aymen Sajjad

#Write a python program to check if a given string is palindrom

def pelindrom(check_str):
   reverse_str="".join(reversed(check_str))
   if check_str==reverse_str:
      return "the string is palindrome"
   else:
      return"not a palindrome"
        
print(pelindrom("aymen"))        