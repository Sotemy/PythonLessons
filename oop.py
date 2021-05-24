#classes in Python
class Dog():
    """Simple model of dog"""

    def __init__(self, name, age):
        """Initialiation of attriute ame and age"""
        self.name = name
        self.age = age
        print(f"Dog {name} created")

    def sit(self):
        """Dog will sit when the command will be called"""
        print(self.name.title() + " sat")

    def jump(self):
        """Dog will jump when the command will be called"""
        print(self.name.title() + " jumped")

    def bark(self):
        print("BARK BARK BARK!!!!")

my_dog = Dog('Chantal', '4')
my_dog2 = Dog('Denis', '14')

print(my_dog.name)
print(my_dog.age)


my_dog.jump()
my_dog2.sit()
poppy = Dog('Poppy', '2')
print(poppy.name)
poppy.bark()