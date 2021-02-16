## Animal наследует object
class Animal(object):
    pass

## дог наследует анимал
class Dog(Animal):

    def __init__(self, name):
        ## композиция имени нейм
        self.name = name

## кот наследует анимал
class Cat(Animal):

    def __init__(self, name):
        ## композиция имени нейм
        self.name = name

## персон наследует объект
class Person(object):

    def __init__(self, name):
        ## композиция имени нейм
        self.name = name

        ## Person – композиция животного некоторого вида
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? хмм, что за чудеса?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## barbos наследует Dog
barbos = Dog("Барбос")

## барсик наследует кот
barsik = Cat("Барсик")

## персон наследует машка
mary = Person("Машка")

## пет - наследник барсик
mary.pet = barsik

## филька - наследник имплои с параметрами филька и 120000
filka = Employee("Филька", 120000)

## пет - наследник барбоса
filka.pet = barbos

## ?? флиппер - сэмпл фиш
flipper = Fish()

## кроуз - сэмпл салмона
crouse = Salmon()

## гарри - сэмпл халибуд
harry = Halibut()