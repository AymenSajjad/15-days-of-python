#Date:29/6/2024
#Author:Aymen Sajjad

#Write a program to check if a given number is a prime number

num=5

flag=True
if num==0:
    flag=False
    if num>1:
     for i in range(1,5):
        if num%i!=0:
            flag=False
        break


if flag==False:
    print("number is not prime")
else:
    print("number is a prime numner")    
