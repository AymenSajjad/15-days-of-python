#Date:7/7/2024
#Author:Aymen Sajjad

#Given a list of words,concatinate them into a single string separated by spaces


def concatination(lst_words):
    string=""
    for i in lst_words:
        string=string+i+" "
    return string


print(concatination(["aymen","Sajjad","alia"]) )   