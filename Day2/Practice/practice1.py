#Date:26/06/2024
#Author:AymenSajjad

#Given a list of numbers ,find the sum and average



#using buit in function


lst_number=[1,2,3,6,8,9]
sum_no=sum(lst_number)         #using built in function sum to calculate the sum of list
print(sum_no)
length_lst = len(lst_number)   #len is built in functin to calculate legth of list
average=sum_no / length_lst    #formula for finding average
print(average)



#without buit in function

lst_number = [1,2,3,6,8,9]
sum_no = 0                                    
length=0
for i in lst_number:
   sum_no += i                               #calculate the sum of all numbers present in list
   length+=1                                 #calculate the length of list
print("the sum of numbers is: ",sum_no)      
print("the length of list is: ",length)


average = sum_no / length                     #formula for finding average
print("the Average of list numbers are : ",average)


