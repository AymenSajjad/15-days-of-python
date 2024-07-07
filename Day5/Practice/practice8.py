#Date:7/7/2024
#Author:Aymen Sajjad

#Given a list of names ,count the number of names that starts with the vowel.

def count_names(name_lst):
    word=0
    vowel="aeiou"
    for i in name_lst:
        if i and i[0] in vowel:
          word+=1
    return word  

print(count_names(["aymen","minal","arfa","saman","faiza","haider"]))