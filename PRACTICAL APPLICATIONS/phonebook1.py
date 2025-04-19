#phonebook using functions
phonebook={}
def addcontact():
    name=input("enter name")
    if name in phonebook:
            print("contact already exist")
    else:
        phone=input("enter phone number")
        phonebook.update({name:phone})
        print(phonebook)
def deletecontact():
    name=input("enter name")
    phone=input("enter phone number")
    phonebook.pop(name)
    print(phonebook)
def updatecontact():
    print("1.name \n 2.phone ")
    option2=int(input("enter the option"))
    if option2==1:
            oldname=input("enter name")
            newname=input("enter name")
            phonebook[newname]=phonebook.pop(oldname)
            print(phonebook)
    if option2==2:
            oldnumber=input("enter phone number")
            newnumber=input("enter new number")
            phonebook[newnumber]=phonebook.pop(oldnumber)
            print(phonebook)
def displaycontact():
      print(phonebook)
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
#             exit()     