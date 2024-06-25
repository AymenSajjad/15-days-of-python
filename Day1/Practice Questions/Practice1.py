#Date:25/6/2024
#Author:Aymen Sajjad

#Write a Python Program to calculate the area of rectanglw given its length and width
#formula: Area of rectangle=Length*width

L=int(input("Enter the Length"))
W=int(input("Enter the Width"))
R=L*W #Formula FOR area Of rectangle
print("Area of rectangle = ",R)



#"""""""""""""""""""Using Function""""""""""""""""""""""""""""""""""""""""""""""""


def Areaofrectangle(L,W):#parameters
    R=L*W #R is for Area of Rectangle L for length and W for Width
    return R

print(Areaofrectangle(3,2)) #Arguments