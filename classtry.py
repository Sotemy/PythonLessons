from datetime import date

class Person(object):
    def __init__(self, age, name):
        self.name = name
        self.age = age
    
    def jump(name):
        print(f"{name} have jumped")

class Dad(Person):
    def __init__(self):
        super(Person.__init__)
    
    def name_myself(myname):
        print(f"my name is {myname}")

    def make_a_son(name_of_son):
        print(f"{name_of_son} is made")

Person.name = "d"
Person.age = 12
print(Person.name)

Person.jump(Person.name)

Dad.name_myself(Person.name)
Dad.make_a_son("patrik")

class Message(object):
    def __init__(self, name, age, time):
        self.name=name
        self.age=age
        self.time=time

    def hello(name):
        print(f"""hello, {name}
You are {Message.age} years old
Now is {Message.time}""")

    
Message.name = "dmitrii"
Message.age = 16
Message.time = date.today()

Message.hello(Dad.name)