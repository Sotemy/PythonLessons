import time, random


random = random.randint(1, 6)

print("""Хочешь сыграть со мной в игру?

(1)Да                                      (2)Нет""")

game = input("> ")

time.sleep(1)

if game == "1":
    print("""На столе лежит кубик. Кинь его. 
Если четное, я проиграл. Нечетно - выиграл.

(1)Кинуть                                   (2)Не кидать""")
    
    cube = input("> ")
    if cube == "1":
        print(f"Тебе выпало {random}")
    elif cube == "2":
        print("ахахах ссыкло")

if game == "2":
    print("ахахах ссыкло")