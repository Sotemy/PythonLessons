# явное наследование

class Parent(object):
    def implicit(self):
        print("PARENT IMPLICIT()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# явное переопределение

class Parent(object):
    def override(self):
        print("PARENT OVERRIDE()")
        years = "40"
        print(f"мне {years} лет")

class Child(Parent):
    def override(self):
        years = "10"
        print(f"мне {years} лет")
        print("ПОТОМОК OVERRIDE()")

dad = Parent()
son = Child()

dad.override()
son.override()