#Date:25/6/2024
#Author:Aymen Sajjad

#Create a Program that take a sentence as input and counts the word  in it
def Sentence(Word):

    word=Word.split() #split method the sentences itto words ,uses white spaces as separator
    
    return len(word) #built in function to calculate length


word_length=input("Enter a Sentence :")

print(Sentence(word_length)) #function Call



