class Animal:  #grand parent class
    def walk(self):
        print("animals can walk")
class Dog(Animal): #parent class
    def bark(self):
        print("dog barking")
class Puppy(Dog):  #child class
    def run(self):
        print("puppy running")
d=Puppy()
d.walk()
d.bark()
d.run()                        