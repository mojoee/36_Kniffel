import random
import collections

class Spieler:
    def __init__(self, name, turn):
        self.score = 0
        self.name  = name
        self.turn  = turn
        self.score = 0
        self.upper_score_sheet = {"1": 0, "2":0, "3":0, "4":0, "5":0, "6":0}
        self.lower_score_sheet = {"3 of a kind": 0, "4 of a kind": 0, "Full house":0, \
            "small straight":0, "large straight":0, "Yatzy":0, "Chance":0, "Bonus": 0}
        self.lower_score_sheet_points= {"3 of a kind": "sum", "4 of a kind": "sum", "Full house":25, \
            "small straight":30, "large straight":40, "Yatzy":50, "Chance":"sum", "Bonus": 50}

    def print_score(self):
        for item, value in {**self.upper_score_sheet, **self.lower_score_sheet}.items():
            #print(item,'------',value)
            print('{:>14} | {:>12}'.format(item, value))
        
    def add_result_to_score(self, result, key):
        if key in self.upper_score_sheet:
            # count occurences in list
            occurrences = collections.Counter(result)
            self.lower_score_sheet[key]=occurrences[int(key)]*int(key)
        elif key in self.lower_score_sheet:
            # if it folllows rule, give bonus points
            points=self.calculate_points(result, key)
            self.lower_score_sheet[key]=points
        else:
            print("key not in result!")

    def roll(self):
        return random.choice(self.results)

    def calculate_points(self, result, key):
        method=self.lower_score_sheet_points[key]
        if method=="sum":
            return sum(result)
        else:
            return method

