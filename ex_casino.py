class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Roulette(Scene):
    def enter(self):
        pass

class Win(Scene):
    def enter(self):
        pass

class Lose(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('roulette')
a_game = Engine(a_map)
a_game.play()