from sys import exit

def dead(why):
    print(why, "Великолепно!")
    exit(0)

def gold_room():
    print("Сколько золота унесешь?")                                        #5               gold   
    choice = input("> ")                                              #4      ktulhu    bear    chan(win)
    if choice == "всё" or choice == "все":                                  #3           tupik    (win)
        print("Ты победитель!!!")                                           #2   rembo  tupik    tupik  dog(win)
    else:                                                                   #start      win         win
        dead("Ты стал бомжом.")

def level_4():
    print("Перед тобой 3 двери:")
    print("\n\tВ первой двери Ктулху. Попробуй задушить!!!")
    print("\n\tВо второй двери Медведь. Зарежь его!!!")
    print("\n\tВ третьей Джеки Чан. Сражайся!!!")
    print("(1)Задушить\t(2)Зарезать\t(3)Сражаться")

    choice = input("> ")
    if choice == "задушить" or choice == "1":
        dead("Ктулху съел тебя.")

    elif choice == "зарезать" or choice == "2":
        dead("Медведь расчленил тебя.")

    elif choice == "сражаться" or choice == "3":
        print("Джеки открыл тебе сокровищницу!")
        gold_room()

    else:
        dead("Животные разорвали тебя на части")

def level_3():
    print("Перед тобой 2 тоннеля:")
    print("\nВыбирай")

    print("\n(1)Пробежать в первом\t(2)Пробежать во втором\t(3)Сбежать назад")

    choice = input("> ")
    if choice == "первый" or choice == "1":
        dead("Ты упал в ловушку.")
    elif choice == "второй" or choice == "2":
        level_4()
    elif choice == "Назад" or choice == "3":
        dead("Пришла собака и укусила тебя.")
    else:
        dead("Животные разорвали тебя на части")

def level_2():
    print("Перед тобой 4 двери. В первой двери стоит Рэмбо и ждет драки. В четвертой - овчарка")
    print("\nВыбирай")
    print("\n(1)Драться\t(2)Вторая\t(3)Третья\t(4)Дразнить")

    choice = input("> ")
    if choice == "драться" or choice == "1":
        print("Ты победил и забрал его перчатки")
        level_3()
    elif choice == "вторая" or choice == "2" or choice == "третья" or choice == "3":
        dead("Ты попал в ловушку")
    elif choice == "дразнить" or choice == "4":
        dead("Тебя укусила собака.")
    else:
        dead("Тебя избил Рэмбо")

def start():
    print("Выбери тоннель")
    print("\n(1)Первый\t(2)Второй")
    
    choice = input("> ").lower
    if choice == "первый" or choice == "1":
        print("БЕГИ!!!!!!!!!!!!!")
        level_2()
    if choice == "второй" or choice == "2":
        print("БЕГИ!!!!!!!!!!!!!")
        level_2()
    else:
        print("Ты пытался выбежать, но убежал во 2 тоннель.")
        level_2()


print("""
_______    __   ___   _______ 
|   ___|  | |   | |   |   ___|
|  |___   | |   | |   |  |___
|____  |  | |  /  |   |____  |
_____| |  | \_/   |   _____| |
|______|  \____/|_|   |______|


GAME



""")

start()