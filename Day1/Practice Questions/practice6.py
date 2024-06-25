#Date:15/6/2024
#Author:Calculate a compound interest of a given priciple amount,interest rate and time period. 

#formula of compound interest
#C=final compound interest amount
#P=initial amount /balance
#r=interest rate
#n=number of times interest applied per time period
#t=total year 
#C=P(1+r/n)^nt

def Compoundinterest(P,r,n,t):
    C=P*(1+r/n)**(n*t)
    return C

print(Compoundinterest(50000,0.1,12,1))


