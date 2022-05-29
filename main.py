from game import Spiel

if __name__=="__main__":
    anzahl_spieler=int(input("How many players for this game? "))
    newGame=Spiel(anzahl_spieler)
    newGame.run()

