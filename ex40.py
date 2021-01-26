class Ex40(object):

    def __init__(self):
 #__инит__ == инициализация объекта
        self.triangle = "треугольник"

    def apple(self):
        print("Я - ЯБЛОКО")

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

thing = Ex40()
thing.apple()
print(thing.triangle)

happy_bday = Song([
    "He могу я тебе в день рождения",

    "Дорогие подарки дарить,",

    "Но зато в эти ночи весенние "])

bulls_on_parade = Song([
  "Далеко-далеко на лугу пасется кто?"
  "Пейте, дети, молоко, будете здоровы!"
])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()