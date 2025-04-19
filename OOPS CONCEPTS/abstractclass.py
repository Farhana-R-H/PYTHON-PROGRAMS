from abc import ABC,abstractmethod
class polygen:
    @abstractmethod  #decorator
    def sides(self):
        pass
class Traingle(polygen):
    def sides(self):
        print("traingle is three sides")
class Pentagon(polygen):
    def sides(self):
        print("pentagon has 5 sides")
t=Traingle()
p=Pentagon()
t.sides()
p.sides()                     