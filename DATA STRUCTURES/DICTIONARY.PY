#dictionary
#dict1={key:value}
# dict1={1:10,2:20,3:30,4:40}
# print(len(dict1))
# print(dict1[1])
# mark=student["mark1"]=60
# print(student)
# name=student["name"]="arun"
# print(student)
# #to remove key
# #student.pop(key)
# #to change name to NAME
# student["NAME"]=student.pop("name")
# print(student)
# student["AGE"]=student.pop("age")
# print(student)
# student["MARK1"]=student.pop("mark1")
# print(student)
# student["MARK2"]=student.pop("mark2")
# print(student)

#methods
# student={"name":"farhana","age":21,"mark1":50,"mark2":55}
# #to get
# print(student.get("mark1"))

# #to add 
# a=student.update({"height":155,"weight":69})
# print(student)

# #remove
# dict1=student.pop("mark2")
# print(dict1)

# #copy and clear
# dict2=student.copy()
# print(dict2)
# print(dict2.clear())

# #list of keys
# print(student.keys())

# #list of key-value pairs
# print(student.items())

# #add using set default
# student.setdefault("mark2",70)
# print(student)

# #get using set default
# print(student.setdefault("age"))

# #list to dict
# list1=[1,2,3,4,5]
# x=100
# print(dict.fromkeys(list1,x))

#loop in dictionary
# student={"name":"farhana","age":21,"mark1":50,"mark2":55}
# #to get keys
# for i in student:
#     print(i)
# #to get values
# for i in student.values():
#     print(i)
# #to get keys and values
# for i,j in student.items():
#     print(i,j)    

#creating a dictionary
# dict1={}
# for i in range(4):
#     k=int(input("enter the key:"))
#     v=int(input("enter the values:"))
#     dict1.update({k:v})
# print(dict1)    

#check is there key in dict
# dict1={1:200,87:21,25:90,3:300}
# n=int(input("enter the key"))
# if n in dict1:
#     print("key is present")
# else:
#     print("key doesnt present")    

#sum all items in a dict
# dict1={1:2,2:3,3:4}
# sum=0
# for i,j in dict1.items():
#     sum+=i+j
# print(sum)    

#rename key in a dict
# dict1={"name":"abc","age":25,"salary":8000,"city":"new york"}
# dict1["location"]=dict1.pop('city')
# print(dict1)

#x,x*x
# dict1={}
# n=int(input("no of keys"))
# for i in range(1,n+1):
#     dict1.update({i:i*i})
# print(dict1)    

#number:its no of occurence as dict
# list1=[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
# list1.sort()
# dict1={}
# for i in list1:
#     dict1.update({i:list1.count(i)})
# print(dict1)    

#concatinate two list to dictionary
list1=["Name", "Age", "Job"]
values = ["shimla",25,"Full Stack Developer"]
book_dict = {}
for i in range(len(list1)):
    book_dict[list1[i]] = values[i]
print(book_dict)
