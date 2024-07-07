#Date:7/7/2024
#Author:Aymen Sajjad

#Given a string,write a function to remove all the vowel from it and return the modified string.

def vowel_removal(string):
    vowel="aeiou"
    modified_str=""
    for i in string:
        if i in vowel:
            continue
        modified_str+=i
        
    return modified_str
 
        
print(vowel_removal("aymen"))
print("vowel removed")
