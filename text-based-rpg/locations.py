import random
import enemy


class Forest:
    def event(self, player):
        turns = 5
        while turns > 0:
            if random.random() < 0.2:
                print("ENEMY ENCOUNTER")
                wolf = enemy.Wolf()
                enemy.combat_loop(wolf, player)
                player.playerUpdate()
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


def explore(location, player):
    if location == "forest":
        forest = Forest()
        forest.event(player)
