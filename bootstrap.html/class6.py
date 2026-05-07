class Animal:
    def eat(self):
        print("Eating.....")

class Dog(Animal):
    def bark(self):
        print("Barking....")

class Puppies(Dog):
    def weap(self):
        print("Weaping....") 

    def eat(self):
        print("Drink milk.....")           
              
o=Puppies()
o.eat()
o.bark()
o.weap()

a=Animal
a.eat()

