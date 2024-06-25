#Date:25/06/2024
#Author:Aymen Sajjad

#write a program that convert a given number of days into year,weeks and days


days=int(input("Enter a Number"))

years=days/365  #365 days in one year
print(years) #print year to check if its give correct answer or not

days_remain=days%365 #remaing days after finding year
print(days_remain) 

weeks=days/7  #weeks in number of days
print(weeks)

remaining_days=days_remain%7  #7 days in week
print(remaining_days)#The remaining days after extracting years and weeks

print(f"{years}: years,{weeks}: weeks,{remaining_days}: days")

