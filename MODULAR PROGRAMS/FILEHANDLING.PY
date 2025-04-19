#File handling
#to read a file
# f=open("D:\python programs\data casting\hello.txt","r")
# data=f.read()
# print(type(data))
# print(data)
# f.close()

#WRITE
#a:append content to existing file,create and write file
# f=open("D:\python programs\data casting\hello.txt","a")
# data=f.write("what is your name? \n my name is farhana")
# f.close()

# #replace existing file
# f=open("D:\python programs\data casting\hello.txt","w")
# data=f.write("how are you? \n im fine")
# f.close()

# #x:only create new file and write
# f=open("newfile.txt","x")
# data=f.write("what is your name? \n my name is farhana")
# f.close()

#using loop
# f=open("newfile","r")
# for i in f:
#     print(i)

#count no of words in a file
# f=open("newfile30.txt","r")
# data1=f.read()
# print(type(data1))
# print(data1)
# list1=data1.split()
# print(list1)
# print(len(list1))
# upper_count=0
# lower_count=0
# for i in data1:
#     if i.isupper():
#         upper_count=upper_count+1
#     else:
#         i.islower()
#     lower_count=lower_count+1
# print("no of upper case:",upper_count)
# print("no of lower case:",lower_count)    

#read lines from text line
# def display_words():
#     f=open("newfile.txt","r")
#     data=f.read()
#     print(data.count("the"))
#     f.close()
# display_words()    

# def display_word():
#     f=open("newfile.txt","r")
#     data=f.read()
#     list1=data.split()
#     for i in list1:
#         if len(i)<4:
#             print(i)
# display_word()   
# def display_word():
#     f=open("newfile.txt","r")
#     data=f.read()
#     list1=data.split()
#     for i in list1:
#         if i[-1]=="e":
#             print(i)
# display_word() 

#line by line to list
# f=open("newfile30.txt","r")
# data=f.read()
# list1=[]
# for i in data:
#     list1.append(i.strp())
# print(list1)


try:
    numer=int(input("enter value"))
    denom=int(input("enter value"))
    res=numer/denom
    print(res)
except ZeroDivisionError:
    print("zero division error occured")   

# try:
#     list1=[2,3,56,44,90]
#     print("index of the number is",list1[int(input("enter a value"))]) 
# except IndexError:
#     print("index out of range")        
    









