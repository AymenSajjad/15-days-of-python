#Date:26/6/2024
#Author:Aymen Sajjad

#create a function to count the number of voxwels in a given string



def vowel_count(vowel_string):
    count=0
    vowel="aeiou"
    for i in vowel_string.lower():
        if i in vowel:
            count+=1
    return "Number of vowel in string is",count


print(vowel_count("Aymenkhan"))
