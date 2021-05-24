import random

class Round():
    def __init__(self, name1, name2):
        self.name1=name1
        self.name2=name2

    def round(self):
        rock = "rock"
        paper = "paper"
        scissors = "scissors"
        print("Выбирай : (R)ock (P)aper (S)cissors")
        answer = input("> ")
        if answer.lower() in ('r', 'p', 's'):
            print(random(1, 7))

i = Round("Dima", "Robot")
i.round()