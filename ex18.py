#2 аргумента
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#2 снова
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#1 аргумент
def print_one(arg1):
    print(f"arg1: {arg1}")

#net argumentov
def print_none():
    print("Я ничего не получаю.")
    
print_two("Михаил","Райтман")
print_two_again("Михаил","Райтман")
print_one("Первый!")
print_none()