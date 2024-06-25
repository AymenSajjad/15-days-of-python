#Date:25/06/2024
#Author:Aymen Sajjad

#Given a list of integers, find the sum of all positive numbers

def lst_integer(Numbers):
    sum_no=0 #intialize the sum to zero

    for i in Numbers: #iterate the list and add upto positive numbers
        if i>0:
            sum_no+=i
    return sum_no  #return sum of all positive numbers in list
    
    
my_list=[1,2,3,4,-4,-5,-7,8]    # define list of integer
lst_integer(my_list)    #Function call




