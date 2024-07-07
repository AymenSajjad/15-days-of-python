#Date:7/7/2024
#Author:Aymen Sajjad

#Create a  function to reverse a given string


def Reverse_string(str_1):
    empty=""
    for i in str_1:
        empty=i+empty
    return empty

print(Reverse_string("ayesha"))
