#Date:7/7/2024
#Author:Aymen Sajjad

#Write a prgram to check if a given string is a pangram(contain all letters of alphabet)

alphabets="abcdefghijklmnopqrstuvwxyz"
pangram="The quick brown fox jumps over the lazy dog"

flag=False
for i in alphabets:
        
    if i in pangram.lower():
        flag=True
    else:
        flag=False
        break
        
if flag==True:
    print("This is a pangram")
else:
    print("This is not a pangram")        