#Date:7/7/2024
#Author:Aymen Sajjad

#Create a function that takes a sentence as input and return the sentense in reverse order.

def reverse_sentence(sentence):
    reversing="".join(reversed(sentence))
    return reversing


input_sentence=input("Enter a sentence: ")
print(reverse_sentence(input_sentence))