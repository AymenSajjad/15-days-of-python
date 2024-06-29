#Date:29/6/2024
#Author:Aymen Sajjad

#Given a list of words,count the number of words with more than five characters

def count_words(lst_word):
    count=0
    for i in (lst_word):
        if len(i)>5:
            count+=1
    return count


print(count_words(["aymen","Minal","subject","object","umama"]))




    