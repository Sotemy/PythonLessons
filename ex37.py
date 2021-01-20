#!/usr/bin/env python
# -*- coding: utf-8 -*-

# попробую написать программу с авторизацией. хз возможен говнокод


import os
from sys import exit

code_frase = "пельмени - это очень вкусно"
login = "123"
password = "123"

def enter():
    print("Чтобы войти, нажмите 1. Введите 2 если забыли пароль")
    vhod = input("> ")
    vhod_est = False
    while vhod_est == False:

        if vhod == "1" and not vhod_est:
            log = input("login > ")
            passwd = input("password > ")
            if log == login and passwd == password:
                print(f"Вы авторизовались как {login}")
                vhod_est = True
                choice()
            elif log != login or passwd != password:   
                #если логин или пароль неравен login или password, то вывод Забыли пароль? Восстановите!. идет повторный опрос login : password
                print("Забыли пароль? Восстановите!")
                vhod_est = False
        elif vhod == "2" and not vhod_est:
            print("Восстановление ")
            restore()
            vhod_est = True
        else:
            print("\nПопробуйте снова\n")
            enter()

def restore():
    print("Введите кодовую фразу :")
    answer = input("> ")
    if answer == code_frase:
        print(f"ваш логин {login} и пароль {password}")
    elif answer != code_frase:
        print("Ban!!!")
        ban()

# def register():
# print("Введите свой id telegram:")
# answer = input("> ")


def ban():
    exit(0)

def sorter():
    print("sssssss  oooooo  rrrrrr  ttttttt  eeeeeee  rrrrrr")
    print("s        o    o  r    r     t     e        r    r")
    print("s        o    o  rrrrrr     t     e        rrrrrr")
    print("sssssss  o    o  r          t     eeeee    r")
    print("      s  o    o  r r        t     e        r r")
    print("      s  o    o  r   r      t     e        r  r")
    print("sssssss  oooooo  r    r     t     eeeeeee  r   r\n\n")
    print(os.listdir())

    print("Выберите файл для нормализации:")
    src = input("> ")
    print("Выберите файл, куда выводить данные:")
    dest = input("> ")
    s = open(src, mode='r')
# s - это source(исходный) файл
    d = open(dest, mode='w')
# d - это destination (конечный) файл
    for line in s:
        d.write(line+':\v')
    print("\nБаза нормализована!\n")
    choice()

def clone():
    print(os.listdir())

    print("Выберите файл для клонирования:")
    src = input("> ")
    print("Выберите файл, в который вывести:")
    dest = input("> ")
    d = open(dest, mode='w')
    s = open(src, mode='r')
    for line in s:
        d.write(line)
    print("\nБаза склонирована!\n\n")

    choice()

def choice():
    print("Выберите программу:")
    print("sorter\texit\tclone")

    answer = input("> ")
    if answer == "sorter":
        sorter()
    elif answer == "exit":
        print("\nВы вышли\n")
        exit(0)
    elif answer == "clone":
        clone()
enter()

