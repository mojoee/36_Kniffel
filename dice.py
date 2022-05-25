import random

class Wuerfel:
    def __init__(self, faces, low, high):
        self.faces = faces
        self.results = list(range(low,high+1))

    def roll(self):
        return random.choice(self.results)