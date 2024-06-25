#Date:25/6/2024
#Author:Aymen Sajjad


#Calculate the sum of Two Numbers Entered bu the user

FirstNo=int(input("Enter a First Number :"))
SecondNo=int(input("Enter a second Number :"))

Sum=FirstNo+SecondNo

print("The sum of Two Numbers is :",Sum)

#""""""""""""""Using Function""""""""""""""""""""""""""""""

def Sum(FirstNo,SecondNo):
    Add=FirstNo+SecondNo
    return Add

print(Sum(9,2) )   