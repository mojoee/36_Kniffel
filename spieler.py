import random

class Spieler:
    def __init__(self, name, turn):
        self.score = 0
        self.name  = name
        self.turn  = turn
        self.score = 0
        self.upper_score_sheet = {"1": 0, "2":0, "3":0, "4":0, "5":0, "6":0}
        self.lower_score_sheet = {"3 of a kind": 0, "4 of a kind": 0, "Full house":0, \
            "small straight":0, "large straight":0, "Yatzy":0, "Chance":0, "Bonus": 0}

    def print_score(self):
        for item, value in {**self.upper_score_sheet, **self.lower_score_sheet}.items():
            print(item,'------',value)
        
    def add_result_to_score(self, result, key):
        if key in self.lower_score_sheet:
            self.lower_score_sheet[key]=result
        elif key in self.upper_score_sheet:
            self.upper_score_sheet[key]=result
        else:
            print("key not in result!")

    def roll(self):
        return random.choice(self.results)