from sys import argv
script = argv
prompt = '> '

print("Введи свое имя, пожалуйста")
user_name = input(prompt)

print(f"Рад знакомству, {user_name}, я - сценарий {script}.")
print("Я хочу задать тебе пару вопросов")
print(f"Я тебе нравлюсь, {user_name}?")
likes = input(prompt)

print(f"Где ты живешь, {user_name}?")
lives = input(prompt)

print("На каком компьютере ты работаешь?")
computer = input(prompt)

print(f"""
Итак, ты ответил {likes} на вопрос, нравлюсь ли я тебе.
Ты живешь {lives}.
И у тебя компьютер {computer}. Прекрасно!!!
""")