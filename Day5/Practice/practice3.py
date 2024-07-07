#Date:7/7/2024
#Author:Aymen Sajjad

#Write a program that take sa sentence as  input and count the number of words in it.


def count_words(sentence):
        sentence_up=sentence.split()
        counting=len(sentence_up)
        return counting
   
inputing=input("Enter a sentence")
print(count_words(inputing))