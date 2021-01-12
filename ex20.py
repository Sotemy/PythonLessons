from sys import argv

print("Введи файл: {input_file}")
script, input_file = argv, input()


# переменная ф читает текст
def print_all(f):
    print(f.read())

# переменная ф "отматывает" файл
def rewind(f):
    f.seek(0)

# line_count - строчка по порядку
# f.readline() - печать строчки
def print_a_line(line_count, f):
    print(line_count, f.readline())


# current_file - этот введенный файл в строке
current_file = open(input_file)


print("Первым делом выведем этот файл целиком:\n")

print_all(current_file)

print("Теперь отмотаем назад, словно это касета.\n")

rewind(current_file)

print("Выведем три строки:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
