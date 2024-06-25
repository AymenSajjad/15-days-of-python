#Date:14/6/2024
#Author:Aymen Sajjad

 
#convert te,perature from celcius to farenheit

C=int(input("Enter a temperature in celcius"))

Farenheit=(9/5)*C+32

print("Here is the temperature from celcius to fahrenheit :", Farenheit)


#""""""""""""""using Function""""""""""""""""""""""""""""""""

def celciustoFaren(Degree):
    Farenheit=(9/5)*Degree+32
    return Farenheit

celciustoFaren(32)