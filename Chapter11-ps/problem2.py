class Animal:
    print("Animal Class")

class Pets(Animal):
    print("Pet class")

class Dog(Pets):

    def bark(self):
        print("Bho Bho....")   

a = Dog()
a.bark()             