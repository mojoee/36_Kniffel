import random
from re import L
from dice import Wuerfel
from spieler import Spieler

class Spiel:
    def __init__(self, players):
        self.players = players
        self.player_list: list[Spieler] = []
        self.wuerfel: list[Wuerfel] = []
        self.anzahl_wuerfel = 5
        
    def create_players(self):
        for i in range(self.players):
            name=input(f"Please enter Player{i}'s name: ")
            self.player_list.append(Spieler(name, i))

    def create_wuerfel(self):
        for i in range(self.anzahl_wuerfel):
            self.wuerfel.append(Wuerfel(6,1,6))
    
    def roll_the_dice(self, n_dice):
        result=[]
        for wuerfel in self.wuerfel[:n_dice]:
            result.append(wuerfel.roll())
        return result

    def player_throw(self, player, n_dice):
        input(f"{player.name}, press enter to throw the dice!")
        result =  self.roll_the_dice(n_dice)
        print(f"Your result is {result}")
        return result

    def player_turn(self, player: Spieler):
        turn_result=[]
        #first and second throw
        for j in range(2):
            if len(turn_result)<5:
                result=self.player_throw(player, 5-len(turn_result))
                answer_choices= " ".join([str(x) for x in list(range(1,6-len(turn_result)))])
                answer = input(f"Which dices would you like to keep? {answer_choices}: ")
                answer = answer.split(' ')
                if answer!=['']:
                    for dice_to_keep in answer:
                        turn_result.append(result[int(dice_to_keep)-1])
                print(f"Your current dice result is {turn_result}")
            else:
                break
        
        #third throw
        if len(turn_result)<5:
            result=self.player_throw(player, 5-len(turn_result))
            turn_result.extend(result)
            print(f"Your current dice result is {turn_result}")
        input("Enter to proceed to score sheet")

        return turn_result

    def add_result_to_sheet(self, player: Spieler, turn_result):
        print(5*'*', "Your current score", 5*'*')
        player.print_score()
        key = input("Where on the score sheet would you like to put your result? ")
        player.add_result_to_score(turn_result, key)
        print(5*'*', "Your updated score", 5*'*')
        player.print_score()

    def one_round(self):
        for player in self.player_list:
            turn_result= self.player_turn(player)
            self.add_result_to_sheet(player, turn_result)
        
    def setup(self):
        self.create_players()
        self.create_wuerfel()
    
    def run(self):
        self.setup()
        for i in range(13):
            self.one_round()
    


        