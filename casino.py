import random, time

print("Добро пожаловать в казино BULBA1337\n")


print("""
╔══╗╔╗╔╦╗─╔══╗╔══╗
║╔╗║║║║║║─║╔╗║║╔╗║
║╚╝╚╣║║║║─║╚╝╚╣╚╝║
║╔═╗║║║║║─║╔═╗║╔╗║
║╚═╝║╚╝║╚═╣╚═╝║║║║
╚═══╩══╩══╩═══╩╝╚╝
─╔╦══╦══╦══╗
╔╝╠═╗╠═╗╠═╗║
╚╗╠═╝╠═╝║─║║
─║╠═╗╠═╗║─║║
─║╠═╝╠═╝║─║║
─╚╩══╩══╝─╚╝
╔══╦══╦══╦══╦╗─╔╦══╗
║╔═╣╔╗║╔═╩╗╔╣╚═╝║╔╗║
║║─║╚╝║╚═╗║║║╔╗─║║║║
║║─║╔╗╠═╗║║║║║╚╗║║║║
║╚═╣║║╠═╝╠╝╚╣║─║║╚╝║
╚══╩╝╚╩══╩══╩╝─╚╩══╝
""")
time.sleep(1)

def choice():
    print("Выберите:\n")
    print("\n(1)Слоты\t(2)Выплаты")

    answer = input("> ")
    if answer == "1":
        slots()

    elif answer == "2":
        print("Вывод от 999.999р")
        exit(0)

def slots():
    print("нажмите 1 чтобы крутить, 2 чтобы выйти:\n")
    num = random.randint(111, 999)
    answer = input("> ")
    if answer == "1":
        print(random.randint(666, 777))
        if num == 777:
            print("WIN")
            exit(0)
        elif num != 777:
            print("Играть еще? нажмите 1 для игры. 2 для выхода")
            answer = input("> ")
            if answer == "1":
                print(random.randint(700, 777))
    elif answer == "2":
        choice()

print("Введите имя:")
name = input("> ")

print(f"Преветствую вас {name}")

print("\nВведите карту для выплат:\n")

card = input("> ")

choice()