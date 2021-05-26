# animal nasleduet object
class Animal(object):

    def jump(self):
        print("I have jumped")

# Dog nasleduet Animal
class Dog(Animal):
    def __init__(self, name):

        self.name = name
        print(f"{name} is here")


class Cat(Animal):

    def __init__(self, name):

        self.name = name
        print(f"{name} is here")

class Person(object):

    def __init__(self, name):

        self.name = name

        # person - komposiziya zhivotnogo nekotorogo vida
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        # ssilka na person
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass


class Salmon(Fish):
    def jumpfromwater():
        print("Salmon have jumped from water")

class Halibut(Fish):
    def hideinsand():
        print("Halibut in sand")

barbos = Dog("Barbos")

barsik = Cat("Barsik")

mary = Person("Mary")

mary.pet = barsik

print(barbos.name)
barbos.jump()
Salmon.jumpfromwater()
Halibut.hideinsand()