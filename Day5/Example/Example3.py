#Date:7/7/2024
#Author:Aymen Sajjad

#Wrtie a function to count a number of vowels in a given string

def check_vowel(str_v):
    count=0
    vowels="aeiou"
    for char in str_v:
        if char in vowels:
           count+=1
    return count
    
print(check_vowel("aymen sajjad"))    