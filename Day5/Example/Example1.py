 #Date:7/7/2024
#Author:Aymen Sajjad

#Create a program to check if a given string is palindrome

def palindrome(Str_1):
    revers_str="".join(reversed(Str_1)).lower()
    if Str_1==revers_str:
        return "The given string is palindrome"
    else:
        return "Not a palindrome"

print(palindrome("tacocat"))
