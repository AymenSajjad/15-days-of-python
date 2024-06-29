#Date:29/6/2024
#Author:Aymen Sajjad

#Write a program that prints all prime numbers between 1 and 50

def is_prime(number):
    flag=True
    if number==0:
        return False
    elif number==1:
        return False
    for i in range(2,number):
        if number%i!=0:
            flag=True

    return flag





print(is_prime(9))

