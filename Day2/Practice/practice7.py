#Date:26/6/2024
#Author:Aymen Sajjad

#Calculate thr area and circumference of a circle given its radius

from math import pi
def areacircum(radius,pi):    #function definition
    area=pi*radius**2          #formula for area of circle
    circumference=2*pi*radius  #formula for circumference of circle
    return area,circumference


print(areacircum(24,pi))    




