#Date:4/07/2024
#Author:Aymen Sajjad


#Given a list of numbers,Create a function to find the sum of all positive numbers


def sum_list(lst):
    sum_list=0
    for i in lst:
        sum_list+=i
    return sum_list

print(sum_list([1,2,4,5,7,8]))