#Date:4/07/2024
#Author:Aymen Sajjad

#Write a function that takes two list and return their intersection(common element)

def intersection(lst1,lst2):
    lst_final=[]
    for i in lst1:
        if i in lst2:
            lst_final.append(i)
    return lst_final

print(intersection([1,2,4,5,6],[3,4,5,6]))


