class Fireball:
    def __init__(self):
        self.name = "Fireball"
    def getName(self):
        return self.name
    def cast(self, player, enemy):
        enemy.hp -= player.attributes["mp"]

class Poison:
    def __init__(self):
        self.name = "Poison"
    def getName(self):
        return self.name
    def cast(self, player, enemy):
        enemy.statuses.append("poison")
        print(enemy.statuses)

class Cure:
    def __init__(self): 
        self.name = "Cure"
    def getName(self):
        return self.name
    def cast(self, player, enemy):
        player.hp += player.attributes["mp"]

class Beserk:
    def __init__(self):
        self.name = "Beserk"
    def getName(self):
        return self.name
    def cast(self, player, enemy):
        pass
        # add beserk attribute to player
