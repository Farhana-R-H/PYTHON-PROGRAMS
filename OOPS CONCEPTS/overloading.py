# class Ship:
#     def move(self):
#         print('ship sails')
# class Car:
#     def move(self):
#         print("we can drive car")
# class Plane:
#     def move(self):
#         print("plane flies") 
# s=Ship()
# c=Car()
# p=Plane()
# for i in (s,c,p):
#     i.move()

#overriding
class Shape:
    def __init__(self,nme):
        self.name=nme
    def area():
        pass
class Square(Shape):
    def __init__(self,nme,len):
        super().__init__(nme)
        self.length=len
    def area(self):
        print("area of square is",self.length**2) 
class Circle(Square):
    def __init__(self,nme,rad):
        super().__init__(nme)
        self.radius=rad
    def area(self):
        print("area of circle is",3.14*(self.radius)**2)
s=Square("square",2)
c=Circle("circle",4)
s.area()
c.area()

#overriding another example:
# class Animal:
#     def __init__(self,nme):
#         self.name=nme
#     def sound():
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("dogs barks")
# class Cat(Dog):
#     def sound(self):
#         print("cats meows")
# d=Dog("dog")
# c=Cat("cat")
# d.sound()
# c.sound()

