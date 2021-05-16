import random, enemy

class Forest:
    def event(self, Player):
        turns = 5
        while(turns > 0):
            if(random.random() < 0.2):
                print("ENEMY ENCOUNTER")
                wolf = enemy.Wolf()
                enemy.combatLoop(wolf, Player)
                Player.playerUpdate()
            else:
                print("You don't encounter anything.")
                input("Continue exploring? (enter)")
                print()
            turns -= 1

class Plains:
    pass
class Village:
    pass
class Dungeon:
    pass
class Wasteland:
    pass
class DragonDen:
    pass

def explore(location, Player):
    if(location == "forest"):
        forest = Forest()
        forest.event(Player)         