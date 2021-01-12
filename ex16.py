from sys import argv

script, filename = argv
print(f"Я собираюсь стереть файл {filename}.")
print("Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C .")
print("Если вы хотите стереть файл, нажмите Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла...")
target.truncate()

print("Теперь я запрашиваю у вас 3 строки.")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("это я запишу.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("и закрою")
target.close