class Song(object):
    def __init__(self, animals_song):
        self.animals_song = animals_song
    
    def sing(self):
        for line in self.animals_song:
            print(line)
            koko = """

            ╔╗─╔╗╔══╗╔═══╗╔═══╗╔══╗
            ║╚═╝║╚╗╔╝║╔══╝║╔══╝║╔╗║
            ║╔╗─║─║║─║║╔═╗║║╔═╗║╚╝║
            ║║╚╗║─║║─║║╚╗║║║╚╗║║╔╗║
            ║║─║║╔╝╚╗║╚═╝║║╚═╝║║║║║
            ╚╝─╚╝╚══╝╚═══╝╚═══╝╚╝╚╝

            """
            print(koko)



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
