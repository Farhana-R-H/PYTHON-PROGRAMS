#OOP

# class Bird:
#     def __init__(self):  #attribute def
#         self.name=" "
#         self.colour=" "
#         self.beak_colour=" "
#     def fly(self):
#         print("birds can fly")
#     def eat(self):
#         print("birds can eat")        
# bird1=Bird()
# bird1.fly()
# bird1.eat()        

#class with attributes
# class Bird:
#     def __init__(self,nme,clr,bkclr):  #attribute def
#         self.name=nme
#         self.colour=clr
#         self.beak_colour=bkclr
#     def fly(self):
#         print("it can fly")
#     def eat(self):
#         print("it can eat")        
# bird1=Bird("CROW","black","grey")
# print(bird1.name)
# bird1.fly()
# bird1.eat()
# print("it is",bird1.colour,"in colour",) 
# print("it has",bird1.beak_colour,"beak")
# bird2=Bird("PARROT","green","red") 
# print(bird2.name)
# bird2.fly()
# bird2.eat()
# print("it is",bird2.colour,"colour")
# print("it has",bird2.beak_colour,"beak")      

#with object and class
# class Bird:
#     def __init__(self):  #attribute def
#         self.name=" "
#         self.colour=" "
#         self.beak_colour=" "
#     def bird_data(self):
#         self.name=str(input("enter name"))
#         self.colour=str(input("enter colour"))
#         self.beak_colour=str(input("enter beak colour"))
#     def print_data(self):
#         print("bird's name:",self.name,", its colour:",self.colour,", its beak colour:",self.beak_colour)        
#     def fly(self):
#         print("it can fly")
#     def eat(self):
#         print("it can eat")        
# bird1=Bird()
# bird1.bird_data()
# bird1.print_data()
# bird1.fly()
# bird1.eat()  

# bird2=Bird()
# bird2.bird_data()
# bird2.print_data()
# bird2.fly()
# bird2.eat()  
#multiple objects
# birds=[]
# for i in range(3):
#     obj=Bird()
#     birds.append(obj)

# for i in birds:
#     i.bird_data()
#     i.print_data()




#class car
# class Car:
#     def __init__(self):
#         self.brandname=" "
#         self.prize=" "
#         self.colour=" "
#     def start(self):
#         print("car is starting")
#     def stop(self):
#         print("car is stopping")        
#     def wheel(self):
#         print("evert car has four wheels")
#     def number_plate(self):
#         print("every car has different number plates")
# #object creation         
# car1=Car()
# car1.start()
# car1.stop()
# car1.wheel()
# car1.number_plate()

#class employee
# class Employee:
#     def __init__(self):
#         self.name=" "
#         self.age=0     
#         self.salary=0
#     def employee_data(self):
#         self.name=str(input("enter name"))
#         self.age=int(input("enter age"))
#         self.salary=int(input("enter salary"))
#     def print_data(self):
#         print("NAME :",self.name, "AGE:",self.age,", SALARY:",self.salary)
# employee1=Employee()
# employee1.employee_data()
# employee1.print_data()                

# employee2=Employee()
# employee2.employee_data()
# employee2.print_data()  

# class Electricity_bill:
#     def __init__(self):
#         self.name=" "
#         self.customer_id=0
#         self.units=0
#         self.total=0
#     def customer_data(self):
#         self.name=str(input("enter name"))
#         self.customer_id=int(input("enter id"))
#         self.unit=int(input("enter units"))
    
#     def calculation(self):
#         if 1<=self.units<100:
#             self.total=self.units*10
#             print("bill is",self.total)
#         elif 100<=self.units<200:
#             self.total=(99*10)+((self.units-99)*15)
#             print("bill is",self.total) 
#         elif 200<=self.units<300:
#             self.total=(99*10)+(99*15)+(self.units-199)*20
#             print("bill is",self.total)
#         elif self.units<=300:
#             self.total=(99*10)+(99*15)+(199*20)+(self.units-299)*25
#             print("bill is",self.total)
# bill=[]
# n=int(input("enter no of customers"))
# for i in range(n):
#     obj=Electricity_bill()
#     bill.append(obj)
# for i in bill:
#     i.customer_data()
#     i.calculation()    

# class Electricity_bill:
#     def __init__(self):
#         self.name = " "
#         self.customer_id = 0
#         self.units = 0
#         self.total = 0
    
#     def customer_data(self):
#         self.name = str(input("Enter name: "))
#         self.customer_id = int(input("Enter customer ID: "))
#         self.units = int(input("Enter units consumed: "))
    
#     def calculation(self):
#         if 1 <= self.units < 100:
#             self.total = self.units * 10
#             print(f"Bill for {self.name} (ID: {self.customer_id}): {self.total}")
#         elif 100 <= self.units < 200:
#             self.total = (99 * 10) + ((self.units - 99) * 15)
#             print(f"Bill for {self.name} (ID: {self.customer_id}): {self.total}")
#         elif 200 <= self.units < 300:
#             self.total = (99 * 10) + (99 * 15) + ((self.units - 199) * 20)
#             print(f"Bill for {self.name} (ID: {self.customer_id}): {self.total}")
#         elif self.units >= 300:
#             self.total = (99 * 10) + (99 * 15) + (99 * 20) + ((self.units - 299) * 25)
#             print(f"Bill for {self.name} (ID: {self.customer_id}): {self.total}")

# bill = []
# n = int(input("Enter number of customers: "))

# for i in range(n):
#     obj = Electricity_bill()
#     bill.append(obj)

# for i in bill:
#     i.customer_data()
#     i.calculation()    

#bookstall
# class Book:
#     def __init__(self):
#         self.title=" "
#         self.author=" "
#         self.price=" "
#     def book_data(self):
#         self.title=input("enter title;")
#         self.author=input("enter author's name:")
#         self.price=int(input("enter price:"))    

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: ${self.price}")

# books=[]
# n=int(input("enter no of books"))
# for i in range(n):
#     obj=Book()
#     books.append(obj)
# for i in books:
#     i.book_data()
#     i.display_info()










# birds=[]
# for i in range(3):
#     obj=Bird()
#     birds.append(obj)

# for i in birds:
#     i.bird_data()
#     i.print_data()

#rectangle
# class Rectangle:
#     def __init__(self):
#         self.length=" "
#         self.breadth=" "
#     def rect_data(self):
#         self.length=int(input("enter length"))
#         self.breadth=int(input("enter breadth"))    
#     def area_data(self):
#         self.area=self.length*self.breadth
#         print("area of rectangle is",self.area)
# # rectangle1=Rectangle()
# # rectangle1.rect_data()
# rectangle1.area_data() 

# class Shopping_cart:
#     def __init__(self):
#         self.name=" "
#         self.price=" "
#         self.quantity=" "
#         self.total=0
#     def product_data(self):
#         self.name=input("enter product name:")
#         self.price=int(input("enter price:"))
#         self.quantity=int(input("enter quantity:"))

#     def calculation(self):
#         self.total=self.price * self.quantity
#         self.total_amount=(self.price * self.quantity)

#     def print_data(self):
#         print(self.name,"\t",
#               self.price,"\t",
#               self.quantity,"\t",
#               self.total,"\t",)
        
          
# cart=[]
# n=int(input("no of products"))
# for i in range(n):
#     obj=Shopping_cart() 
#     cart.append(obj)
# for i in cart:
#     i.product_data()
#     i.calculation()
# print("name","\t","price", "quantity",  "total",)
# for i in cart:
#     i.print_data()




# for i in students:
#     i.student_data()
#     i.calculation()
#     i.student_grade()
# print("name","\t","roll no","\t","total","\t","grade","\t")    
# for i in students:
#     i.print_data()


#user login
objectlist={}
class Login:
    def __init__(self):
        self.user=""
        self.pas=""
    def data(self):
        self.user=input("enter username")
        self.pas=input("enter password")
        objectlist.update({self.user:self.pas})
    def display(self):
        print(objectlist)

log=[]
for i in range(3):
    obj=Login()
    log.append(obj)

for i in log:
    i.data()
    i.display()


