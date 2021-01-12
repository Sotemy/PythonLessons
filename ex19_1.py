def money(banknotes, coins):
    print(f"мы получили : \n{banknotes} купюр")
    print(f"{coins} монет")
    print(f"Суммарно это ", coins + banknotes , " объектов")


#####################################

print("Рассчитаем прибыль за сегодня:")
money(20, 30)

print("\nРассчитаем прибыль за вторник:")
today_banknotes = 20
today_coins = 30

money(today_banknotes + 20, today_coins + 5)

print("\nРассчитаем прибыль за среду:")
money(40 + 100, 35 + 40)

print("\nСо среды по пятницу магазин не работал, поэтому итоги недели:")
money(20 + today_banknotes + 20 + 40 + 100, today_coins + today_coins + 5 + 35 + 40)

#####################################

x, y = int(input()), int(input())

print("\nРассчитаем прибыль в понедельник:")
money(x, y)

print("\nРассчитаем прибыль во вторник:")
money(x * 2, y * 2)

print("\nРассчитаем прибыль в среду:")
money(x * 2, y * 2)

print("\nРассчитаем прибыль в четверг")
money(20, 20)

print("\nРассчитаем прибыль в пятницу:")
money(x * 2 + 20, y * 2)

print("\nИтоги недели:")
money(x * 7 + 40, y * 7 + 20)
