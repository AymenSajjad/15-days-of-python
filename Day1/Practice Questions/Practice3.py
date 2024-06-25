#Date:25/6/2024
#Author:Aymen Sajjad

#write a Program to check if a number is even or odd

Number=int(input("Enter a Number"))
if Number%2==0:
    print("The number is odd")
else:
    print("The number is Even")    


#Using Function

def EvenOdd(Number):
    if Number%2==0:
        return "Number is even"
    else:
        return "Number is Odd"

print(EvenOdd(3))        