#Date:26/6/2024
#author:Aymen Sajjad

#Write a prgram to check if a given string is a pangram(contain all letters of alphabet)

pangram="How quickly daft jumping zebras vex!"
alphabets="a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
flag=False
for i in alphabets:
        
    if i in pangram.lower():
        flag=True
    else:
        flag=False
        break
        
if flag==True:
    print("This is a pangram")
else:
    print("This is not a pangram")        

