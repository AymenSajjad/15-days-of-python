#Date:26/6/2024
#Author:Aymen sajjad

#write a program to check if a number is prime


number=7
flag=True

if number==1:
     flag=False
elif number>1:
    for i in range(2,number):
    
        if number%i==0:
            flag=False
            break
print(flag)        

if flag==False:
    print(f"{number}is not a prime number")
else:
    print(f"{number}is a prime number")    

