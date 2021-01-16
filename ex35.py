from sys import exit

def gold_room():
    print("Здесь полно золота. Сколько кг ты унесешь?")

    choice = input("> ")
    if choice < 1:
        how_much = int(choice)
    else:
        dead("вводи")

    if how_much < 50:
        print("Шикарно! Ты не жадный, поэтому выигрываешь!")
        exit(0)
    else:
        dead("zhadina")



def bear_room():
    print("zdecb сидит медведь.")
    print("У медведя бочка с медом.")
    print("Медведь закрыл собой дверь выхода.")
    print("KaK переместить медведя? Отобрать мед или подразнить медведя?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "отобрать мед":
            dead("Медведь посмотрел на тебя и ударил лапой по лицу.")
        elif choice == "подразнить медведя" and not bear_moved:
            print("Медведь отошел от двери.")
            print("Вы можете войти в нее. Подразнить медведя или войти в дверь?")
            bear_moved = True
        elif choice == "подразнить" and bear_moved:
            dead("Медведь разозлился и откусил тебе ногу.")
        elif choice == "войти" and bear_moved:
            gold_room()
        else:
            print("Введите одно из предложенных действий.")


def ktulhu_room():
    print("Ha тебя смотрит великий и ужасный Ктулху.")
    print("Он смотрит на тебя, и ты начинаешь сходить с ума.")
    print("Убежать или начать сражаться?")

    choice = input("> ")

    if "убежать" in choice:
        start()
    elif "сражаться" in choice:
        dead("XM, возможно, даже удастся победить!")
    else:
        ktulhu_room()


def dead(why):
    print(why, "Великолепно!")
    exit(0)

def start():
    print("Ты в темной комнате.")
    print("OTCюдa ведут две двери, налево и направо.")
    print("Куда ты повернешь?")

    choice = input("> ")

    if choice == "налево":
        bear_room()
    elif choice == "направо":
        ktulhu_room()
    else:
        dead("bt ходишь из комнаты в комнату, пока не умираешь с голоду.")


start()