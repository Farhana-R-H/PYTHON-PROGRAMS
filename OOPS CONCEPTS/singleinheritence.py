#single inheritance
# class Animal:
#     def __init__(self,nme,clr):
#         self.name=nme
#         self.colour=clr
#     def data(self):
#         print(self.name,"is",self.colour,"in colour")

# class Bird(Animal):
#     #add new attribute by keeping old attributes
#     def __init__(self,nme,clr,bkclr):
#         super().__init__(nme,clr)
#         self.beakclr=bkclr
#     def beak(self):
#         print("it has",self.beakclr,"beak")    
#     def fly(self):
#         print(self.name,"can fly") 
# birds=Bird("parrot","green","red")
# birds.data()        
# birds.fly()
# birds.beak()

#vehicle
class Vehicle:
    def __init__(self,nme,clr):
        self.name=nme
        self.colour=clr
    def data(self):
        print(self.name,"is in",self.colour,"colour")
class Car(Vehicle):
    def __init__(self,nme,clr,whl):
        super().__init__(nme,clr)
        self.wheel=whl
    def info(self):
        print(self.name,"has",self.wheel,"wheels")
car=Car("SWIFT","WHITE","4") 
car.data()
car.info()

        
        
