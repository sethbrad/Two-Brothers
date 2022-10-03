class Spell:
    def get_name(self):
        return self.name

class Fireball(Spell):
    def __init__(self):
        self.name = "Fireball"
    def cast(self, player, enemy):
        enemy.hp -= player.attributes["mp"]

class Poison(Spell):
    def __init__(self):
        self.name = "Poison"
    def cast(self, player, enemy):
        enemy.statuses.append("poison")
        print(enemy.statuses)

class Cure(Spell):
    def __init__(self): 
        self.name = "Cure"
    def cast(self, player, enemy):
        player.hp += player.attributes["mp"]

class Beserk(Spell):
    def __init__(self):
        self.name = "Beserk"
    def cast(self, player, enemy):
        pass
        # add beserk attribute to player
