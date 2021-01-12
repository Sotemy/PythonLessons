def cheese_and_crackers(cheese, crackers):
    print(f"У нас есть {cheese} сырков!")
    print(f"У нас есть {crackers} пачек чипсов!")
    print("этого достаточно для вечеринки!")
    print("Погнали!\n")


print("Мы можем непосредственно передать числа функции:")
cheese_and_crackers(20, 30)


print("Или, мы можем использовать переменные из нашего сценария:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("Мы можем выполнить вычисления внутри функции:")
cheese_and_crackers(1 + 5, 6 + 7)


print("И объединить переменные с вычислениями:")
cheese_and_crackers(amount_of_cheese + 30, amount_of_crackers + 80)