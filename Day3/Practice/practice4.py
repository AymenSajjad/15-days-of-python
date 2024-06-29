#Date:29/6/2024
#Author:Aymen Sajjad

#create a program that generates a fibonacci sequence upto a given number of terms

number=8
lst=[0,1]
if number<=0:
    print ("Enter a positive number")
elif number==1:
    print(0)
elif number==2:
    print(lst)
elif number>2:
    for i in range(3,number):
        lst_1=lst[-1]+lst[-2]
        lst.append(lst_1)
        print(lst)



