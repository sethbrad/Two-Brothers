LEVELUP_XP_MULTIPLIER = 1.1


class Hero:
    attributes = {
        "hp": 100,
        "stamina": 100,
        "mana": 100,
        "strength": 5,
        "toughness": 5,
        "mp": 5,
        "evasiveness": 5
    }
    player_level = 1
    player_class = ""
    next_level_xp = 50
    xp = 0

    inventory = {
        "weapons": [],
        "armor": [],
        "spells": [],
        "items": [],
        "gold": 0
    }

    def player_update(self):
        if self.xp > self.next_level_xp:
            self.xp = self.xp - self.next_level_xp
            self.next_level_xp = 50 * (LEVELUP_XP_MULTIPLIER**(self.player_level - 1))

            print("You leveled up!")
            self.player_level += 1
            self.specialize()

    def specialize(self):
        print("1 point remaining.")
        attr = input("Choose an attribute to level up: ")

        if attr == "hp":
            self.attributes["hp"] += 10
        elif attr == "stamina":
            self.attributes["stamina"] += 10
        elif attr == "mana":
            self.attributes["mana"] += 10
        elif attr == "strength":
            self.attributes["strength"] += 1
        elif attr == "toughness":
            self.attributes["toughness"] += 1
        elif attr == "mp":
            self.attributes["mp"] += 1
        elif attr == "evasiveness":
            self.attributes["evasiveness"] += 1
        else:
            print("Invalid attribute choice.")
            self.specialize()

        print("No points remaining. Level up successful.")

    def choose_class(self):
        print("AVAILABLE CLASSES --> Rogue, Mage, Warrior, Healer")

        choice = input("Enter a class: ")

        if choice == "rogue":
            self.attributes["evasiveness"] += 2
            self.attributes["stamina"] += 20
            self.player_class = "Rogue"
            self.inventory["spells"].append("poison")
        elif choice == "mage":
            self.attributes["mp"] += 2
            self.attributes["mana"] += 20
            self.player_class = "Mage"
            self.inventory["spells"].append("fireball")
        elif choice == "warrior":
            self.attributes["strength"] += 2
            self.attributes["hp"] += 20
            self.player_class = "Warrior"
            self.inventory["spells"].append("beserk")
        elif choice == "healer":
            self.attributes["toughness"] += 2
            self.attributes["mana"] += 20
            self.player_class = "Healer"
            self.inventory["spells"].append("cure")
        else:
            print("Invalid class")
            self.choose_class()
