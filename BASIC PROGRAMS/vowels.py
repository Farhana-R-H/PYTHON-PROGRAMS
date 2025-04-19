#count vowels
# txt=str(input("enter the sentence:"))
# count=0
# for i in txt:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         count=count+1
# print("no of vowels in the sentence is",count) 


#alternative charecters into upper case
# txt=str(input("enter the sentence:"))
# res=" "
# for i in range(len(txt)):
#     if i%2==0:
#         res=res+txt[i].upper()
#     else:
#         res=res+txt[i].lower()
# print(res)        

#vowels in a file
# f=open("newfile.txt","r")
# data=f.read()
# count=0
# for i in data:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         count+=1
# print("number of vowels present in the file is:",count)        


f=open("newfile30.txt","r")
data=f.read()
count=0
for i in data:
    if i.isdigit()==True:
        count+=1
print("No of digits present:",count)        