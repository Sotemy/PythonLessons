class Song(object):
    def __init__(self, animals_song):
        self.animals_song = animals_song
    
    def sing(self):
        for lines in self.animals_song:
            print(lines)

cats_song = Song([
    "МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ ",
    "МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ",
    "МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ \n"
])

dogs_song = Song([
    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ",
    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ",
    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ",
    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ"
])
cats_song.sing()
dogs_song.sing()

class Cat(object):
    def __init__(self):
        self.name = "Alisa"
        self.color = "brown"
        self.years = "2"
        print(f"Я кошка {self.name}. мне {self.years} года и я {self.color} цвета")

cat = Cat()
print(f"Я кошка {cat.name}. мне {cat.years} года и я {cat.color} цвета")

