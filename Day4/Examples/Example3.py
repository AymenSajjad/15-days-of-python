#Date:4/07/2024
#author:Aymen Sajjad

#Implement a function that reverses a given string

def reverse_string(str_rev):
    reversing=""
    for i in str_rev:
        reversing=i+reversing
    return reversing
    
print(reverse_string("aymen") )   