# coding: utf8
from sys import argv

#otkritie faila
script = argv
print("Bведи имя файла :")
filename = input()

txt = open(filename, encoding='utf-8')

print(f"Содержимое файла {filename}:")
print(txt.read())

print("Снова введите имя файла:")
file_again = input("> ")

txt_again = open(file_again, encoding='utf-8')

print(txt_again.read())

txt.close()
txt_again.close()