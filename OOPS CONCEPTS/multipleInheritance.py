#multiple inheritence 
class Parent_class1:
    def __init__(self,nme):
        self.name=nme
    def Addition(self,a,b):
        return a+b
    def print_data(self):
        print("Parent_class1")
class Parent_class2:
    def __init__(self,typ):
        self.type=typ
    def Multiplication(self,a,b):
        return a*b
    def print_data(self):
        print("Parent_class2")
class Derived(Parent_class1,Parent_class2):
    def Division(self,a,b):
        return a/b
d=Derived(" ")
#d.print_data()
Parent_class1.print_data(d)
Parent_class2.print_data(d)
print("addition is",d.Addition(10,20))                    
print("multiplication is",d.Multiplication(10,20))
print("division is",d.Division(10,20))