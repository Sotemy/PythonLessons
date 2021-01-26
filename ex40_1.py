class Song(object):
    def __init__(self, animals_song):
        self.animals_song = animals_song
    
    def sing_me_a_song(self):
        for line in self.animals_song:
            print(line)

cats_song = Song([
    "МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ ",

    "МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ",

    "МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ \n"
])

dogs_song = Song([
    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ",

    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ",

    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ",

    "ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ ГАВ "
])
cats_song.sing_me_a_song()
dogs_song.sing_me_a_song()
