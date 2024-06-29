#Date:20/6/2024
#Author:Aymen Sajjad

#given a list of integers,find all the even numbers and store them in a new list

def is_even(lst_1):
    lst_2=[]
    for i in lst_1:
        if i%2==0:
            lst_2.append(i)
    return lst_2


print(is_even([1,2,3,8,4,6,10]))