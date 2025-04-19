#LIST[]
# list1=[10,28,"bye",7.2,"hello"]
# print(list1)
#indexing
# print(list1[2])
# print(list1[0:4])
# print(list1[:1])
# print(list1[-5:])
#proof for list is mutable
#mofify
# list1[0]=100
# print(list1)
#add an element to the end
# list1.append("moon")
# print(list1)
#remove an element 
# list1.remove("bye")
# print(list1)
#to add element in between numbers
# list1.insert(3,10.5)
# print(list1)
#to add multiple elements at a time
# list1.extend([23,45.9,"sun"])
# print(list1)
#deletion of elements
#last element
#elements at any position
# list1.pop(5)
# print(list1)
#number of occurence
# print(list1.count(100))
#first occurence position
# print(list1.index(28))
#to copy list1 to another
# list2=list1.copy()
# print(list2)
#clear
# list2.clear()
# print(list2)











#sorting list
# list3=[1,100,56.8,89,10,33.5]
# list3.sort()
# print(list3)






















#descending order
# list3.sort(reverse=True)
# print(list3)
#to reverse original list
# list1.reverse()
# print(list1)


#sum of elements in a tuple
# tuple1=(2,4,6,8,10)
# list1=[]
# list1=list(tuple1)
# sum=0
# for i in list1:
#     list1.append(i)
#     sum=sum+i
# print(list1)
# print(sum)    







#program to create a int list and sum of all list elements
# list1=[]
# sum=0
# for i in range(6):
#     item=int(input("enter elements:"))
#     list1.append(item)
#     sum=sum+item
#     print(list1)
#     print(sum)

#using function
# list1=[]
# def sum_of_elements():
#     n=int(input("enter no of elements:"))
#     sum=0
#     for i in range(n):
#         item=int(input("enter elements:"))
#         list1.append(item)
#         sum=sum+item
#         print(list1)
#         print(sum)
# sum_of_elements()    

#find second largest element from a list
# list1=[]
# l=0
# n=int(input("enter value:"))
# for i in range(n):
#     item=int(input("enter the elements:"))
#     list1.append(item)
# list1.sort()
# print(list1)
# print(list1[n-2],"is the second largest element")    








#frequency count
# list1=[1,23,44,1,44,56,3,78,3,100,20,100,100,3,3,1]
# n=int(input("enter the number"))
# print(n,"has occured",list1.count(n),"times")














#input a sentence and print words in it
# sent=str(input("enter the sentence:"))
# list1=sent.split()
# for i in list1:
#     print(i)

#count number of words in a sentence
# txt=str(input("enter the sentence:"))
# list1=txt.split()
# print(list1)
# print(len(list1))   

#sort words of sentence in ascending order
# txt=str(input("enter the sentence:"))
# list1=txt.split()
# list1.sort()
# print(list1)

#find the largest word in sentence
# txt=str(input("enter the sentence"))
# list1=txt.split()
# large=list1[0]
# for i in range(1,len(list1)):
#     if len(list1[i])>len(large):
#         large=list1[i]
# print(large)        

#FEBRUARY 6

#to find no of elememts in between 
# list1=[2,5,34,23,49,44,22,9]
# up=int(input("value1:"))
# low=int(input("value2:"))
# count=0
# for i in list1:
#     if i>low and i<up:
#         count+=1
# print(count)


#
# list1=["hi","hello","good","yes"]
# print(list1[0])
# print(list1[1].upper())
# print(list1[3].replace("yes","no"))
# print(list1[0].replace("i","!"))
# print(list1[2][2])

# list1=["hi","hello","eye","yes"]
# for i in list1:
#     if len(i)>=2 and i[0]==i[-1]:
#          print(i)      
# 
# list1=[1,3,12,[8,9],24,25] 
# print(list1[3][1])
# list1[3].append(10)
# print(list1) 
# list2=[10,56,[2,4,6,[89,67],100],21,45]
# print(list2[2])
# #to access 67
# print(list2[2][3][1])

# list1=[10,20,[30,40,[50,60],50],30,40]
# #add item 70 after 60
# list1[2][2].append(70)
# print(list1)

# list1=[11,[22,33],44,550]
# #modify 22 to 222
# list1[1][0]=222
# print(list1)

# list1=[2,3,20,35,89,90]
# # i=list1.index(20)
# # if list1.count(20)>=1:
# #     list1.remove(20)
# #     list1.insert(i,200)
# #     print(list1)

# if 20 in list1:
#     pos=list1.index(20)
#     list1[pos]=200
#     print(list1)    

#remove odd
# list1=[2,3,4,5,6,7,8,9,11,20]
# reslist=[]
# for i in list1:
#     if i%2==0:
#         reslist.append(i)
# print(reslist)        

#circular right
# list1=[1,2,3,4,5]
# print(list1[-1:]+list1[0:-1])

#mk gandhi
# name=str(input("name:"))
# list1=name.split()
# n=list1[0][0].upper()+" "+list1[1][0].upper()+" "+list1[2].capitalize()
# print(n)

#delet the word "the"
# word=str(input("sentence:"))
# list1=word.split()
# res=[]
# for i in list1:
#     if i!="the":
#         res.append(i)
# res=" ".join(res) 
# print(res)       

#remove all duplicate words
# word=str(input("enter the sentence"))
# list1=word.split()
# res=[]
# for i in list1:
#     if i not in res:
#         res.append(i)
# res=" ".join(res)
# print(res)        





# word=input("Enter the sentence: ")      
# list1=word.split()
# res=[]
# s=set()

# for i in list1:
#     if i not in s:
#         res.append(i)
#         s.add(i)  

# res = " ".join(res)
# print(res)        

#
# list1=[2,4,5,7,3,22,5,11,67]
# res=[]
# for i in list1:
#     if i>1:
#         is_prime=True
#         for j in range(2,(i//2)+1):
#             if i%j==0:
#                 is_prime=False
#                 continue
#         if is_prime:
#             res.append(i)
# print("prime numbers:",res)          
# 
# list1=[1,2,4,5,7,9,40,11,68,85,8,33]
# even=[]
# odd=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even list",even)
# print("odd list",odd)                 


# tuple1=(4,98,75,4,7,31,90,78,4,1,0,23)
# n=int(input("enter element"))
# count=0
# for i in tuple1:
#     if i==n:
#         count=count+1
# print("count of elements:",count)        

set1={1,2,3,4,5,6,9}
for i in set1:
    if i%2==1:
        print(i)