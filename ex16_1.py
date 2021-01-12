from sys import argv

script, filename = argv

txt = open(filename, encoding='utf-8')

print(F"Я собираюсь прочитать файл {filename}")
print(f"Содержимое файла {filename}:")
print(txt.read())

print(f"Если хотите перезаписать файл, нажмите Enter. Если нет, напишите CTRL+C")

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

target.write(f'{line1}\n{line2}\n{line3}')


print("и закрою")
target.close