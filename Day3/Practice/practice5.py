#Date:29/6/2024
#Author:Aymen Sajjad

#Given a list of names,print a name string starting with letter 'A'.


#first method
def Name_A(name):
    for i in name:
        if "A" in i[0]:
            print(i)

Name_A(["Aymen","maryam","Ayesha","Asad"])




#using built in function

def Name_a(name_2):
    
    for i in name_2:
        if i.startswith("A"):
            print (i)    
name_list=["Aymen","maryam","Ayesha","Asad"]
Name_a(name_list)

