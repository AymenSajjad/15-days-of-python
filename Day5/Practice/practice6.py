#Date:7/7/2024
#Author:Aymen Sajjad


#Write a python program to find the length of longest string in a sentence

def string_length(sentence):
    new_sentence=sentence.split()
    long_string=""
    for i in new_sentence:
        if len(i)> len(long_string):
            long_string=i
            length=len(i)
            
    return length
    
print(string_length("my name is aymen"))   
                        
