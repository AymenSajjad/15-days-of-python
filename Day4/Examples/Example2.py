#Date:4/07/2024
#author:Aymen Sajjad

#create a function to check if a number is prime

def is_prime(num):
 divisor=2
 if num%divisor==0:
    return False
 print("num is: ",num)
 print("divisor is",divisor)
 divisor+=1
 return True

for i in range(1,20):
  if is_prime(i+1):
    print(i+1)    