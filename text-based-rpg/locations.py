import random, enemy

class Forest:
    def event(self):
        turns = 5
        while(turns > 0):
            if(random.random() < 0.2):
                print("Enemy encounter")
                wolf = enemy.Wolf()
                enemy.enterCombat(wolf)
            else:
                print("You don't encounter anything.")
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

def explore(location):
    if(location == "forest"):
        forest = Forest()
        forest.event()         