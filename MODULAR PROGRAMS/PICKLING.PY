#pickling
# import pickle
# #define python object
# person={"name":"farhana",
#         "age":21,
#         "place":"thrissur"}
# #pickling=write the object to binary form
# with open("person.pickle","wb") as file:
#     pickle.dump(person,file)
# #unpickling=load a data from a file
# with open("person.pickle","rb") as f:
#     data=pickle.load(f)
#     print(data)   

# from phonebook1 import *
# while(True):
#       print("MENU \n 1.Add \n 2.Delete \n 3.Update \n 4.Display \n 5.Exit")
#       option=int(input("enter choice"))
#       if option==1:
#             addcontact()
#       elif option==2:
#             deletecontact()
#       elif option==3:
#             updatecontact()
#       elif option==4:
#             displaycontact()
#       elif option==5:
#             f=open("contact1.txt","a")
#             for i,j in phonebook.items():
#                   f.write(i+":"+str(j)+"\n")
#             exit()     


# import pickle
# n=int(input("enter the number of students:"))
# for i in range(n):
#     name=input("enter name:")
#     rollno=int(input("enter roll no:"))
#     date_of_birth=input("enter dob:")
#     student=print(name,rollno,date_of_birth)
# with open("student.pickle","wb") as file:
#     pickle.dump(student,file) 
# print("pickling completed")   


import pickle
n=int(input("enter the number of employees:"))
for i in range(n):
    name=input("enter name:")
    age=int(input("enter age:"))
    id=input("enter id:")
    employee=print(name,age,id)
with open("employee.pickle","wb") as file:
    pickle.dump(employee,file) 
print("pickling completed")   