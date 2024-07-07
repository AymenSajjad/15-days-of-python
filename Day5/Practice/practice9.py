
#Date:7/7/2024
#Author:Aymen Sajjad

#Write a function to remove all duplicate characters from a given string

def duplication_remove(string):
    new_string=""
    for i in string:
        if i not in new_string:
            new_string+=i 
    return new_string


print(duplication_remove("muzzamil"))



