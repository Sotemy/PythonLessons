print("Давайте попрактикуемся:")
print('Вы должны знать об упрвляющих последовательностях с символом \\, которые:')
print('\n управляют переносом строк и \t отступами.')

poem = """
\tДля счастья
мне совсем немного надо
хочу тебя \n я нежно обнимать
хочу всегда
я быть с тобою рядом
\n\t\tи никогда не отпускать!
"""

print("-------------------------------------------------")
print(poem)
print("-------------------------------------------------")


five = 10 - 2 + 3 - 6
print(f"Здесь 5: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)


print("Начиная с: {}".format(start_point))

print(f"У нас есть {beans} бобов, {jars} банок и {crates} ящиков")

start_point = start_point / 10

print("Мы такжже можем сделать это таким образом:")
formula = secret_formula(start_point)

print("У нас есть {} бобов, {} банок и {} ящиков".format(*formula))