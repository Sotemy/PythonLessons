#       вш1                                 вш2
#        |                                   |
# __________________________________________________
# (_________________________________монтер__________)
#      ()
#      |              ___________            | Д
#      |_________()  |бункер     |           | Е
#       _____        |___________|           | П
#       |кпп|________________________________| О
#  ______|__________________________________________
# (_________________________________________________)
#        |                                   |
#       вш3                                 вш4
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
import time
from sys import exit
from playsound import playsound

def dead():
    print("Тебя поймали монтеры.")
    playsound('dead.mp3')
    exit(0)

def bunker():
    print("Тут Котофей, биг бро. Да вообще все")
    playsound('win.mp3')
    exit(0)

def luk():
    print("Полезем в люк?")
    playsound('win.mp3')
    print("\n(1)Да\t(2)Нет")
    luk_open = False
    while True:
        answer = input("> ")
        
        if answer == "да":
            print("Люк открыт. Боно, открывай гирмодверь!")
            bunker()


        elif answer == "нет" and not luk_open:

            print("Попробуем вскрыть люк?")
            luk_open = True
            
            answer = input("> ")
            if answer == "да":
                bunker()
            else:
                dead()

def tunnel1():
    print("Ты в тоннеле. монтер в другом конце тоннеля. Побежать к люку?")
    playsound('monter.mp3')
    print("\n(1)Да\t(2)Нет")

    answer = input("> ")
    if answer == "да":
        print("ты убежал от монтеров. Лезем в люк?")
        print("\n(1)Да\t(2)Нет")

        answer = input("> ")
        if answer == "да":
            luk()
        elif answer == "нет":
            dead()

    elif answer == "нет":
        dead()

def vent3():
    print("Лезем в эту шахту?")
    answer = input("> ")

    if answer == "да":
        print("Ты в тоннеле")
        tunnel1()
    elif answer == "нет":
        dead()

def vent4():
    print("Лезем в эту шахту?")
    answer = input("> ")

    if answer == "да":
        print("Ты в тоннеле, но тут монтер")
        playsound('dead.mp3')
        dead()
    elif answer == "нет":
        dead()

def tunnel2():
    print("тут нет монтеров. пошли через кпп")
    print("\t(1)да    (2)нет")

    answer = input("> ")
    if answer == "да":
        dead()
    else:
        dead()

def vent2():
    print("Лезем в эту шахту?")
    answer = input("> ")

    if answer == "да":
        print("Ты в тоннеле, но тут монтер")
        playsound('dead.mp3')
        dead()
    elif answer == "нет":
        dead()

def vent1():
    print("Лезем в эту шахту?")
    answer = input("> ")

    if answer == "да":
        print("Ты в тоннеле")
        tunnel2()
    elif answer == "нет":
        playsound('dead.mp3')
        dead()

def start():
    print("Какую шахту выберешь?")
    print("\n1\t2\t3\t4")
    
    answer = input("> ")
    if answer == "1":
        vent1()
    elif answer == "2":
        vent2()
    elif answer == "3":
        vent3()
    elif answer == "4":
        vent4()
    else:
        playsound('monter.mp3')
        print("Тебя бабушки прогнали")
start()