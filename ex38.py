ten_things = "Яблоки Апельсины Вороны Телефоны Свет Сахар"
stuff = ten_things.split(' ')
more_stuff = ["День", "Ночь", "Песня", "Мишка", "Кукуруза", "Банан", "Девочка", "Мальчик"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("добвляем: ", next_one)
    stuff.append(next_one)
    print(f"Теперь тут {len(stuff)} объектов")

print("all:", stuff)
print("2 object:", stuff[1])
print(stuff.pop())
print("all:", stuff)
print("last object:", stuff[-1])
print(' '. join(stuff))
print("all:", stuff)
print(' и '.join(stuff[3:5]))