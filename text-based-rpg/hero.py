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
    playerLevel = 1
    playerClass = ""
    nextLevelXP = 50
    XP = 0

    inventory = {
        "weapons": [],
        "armor": [],
        "spells": [],
        "items": [],
        "gold": 0
    }

    def playerUpdate(self):
        if(self.XP > self.nextLevelXP):
            self.XP = self.XP - self.nextLevelXP
            self.nextLevelXP = 50*(1.1**(self.playerLevel-1))
            
            print("You leveled up!")
            self.playerLevel += 1
            self.specialize()


    def specialize(self):
        print("1 point remaining.")
        attr = input("Choose an attribute to level up: ")

        if(attr == "hp"):
            self.attributes["hp"] += 10
        elif(attr == "stamina"):
            self.attributes["stamina"] += 10
        elif(attr == "mana"):
            self.attributes["mana"] += 10
        elif(attr == "strength"):
            self.attributes["strength"] += 1
        elif(attr == "toughness"):
            self.attributes["toughness"] += 1
        elif(attr == "mp"):
            self.attributes["mp"] += 1
        elif(attr == "evasiveness"):
            self.attributes["evasiveness"] += 1
        else:
            print("Invalid attribute choice.")
            self.specialize()
            
        print("No points remaining. Level up successful.")

    def chooseClass(self):
        print("AVAILABLE CLASSES --> Rogue, Mage, Warrior, Healer")

        choice = input("Enter a class: ")

        if(choice == "rogue"):
            self.attributes["evasiveness"] += 2
            self.attributes["stamina"] += 20
            self.playerClass = "Rogue"
            self.inventory["spells"].append("poison")
        elif(choice == "mage"):
            self.attributes["mp"] += 2
            self.attributes["mana"] += 20
            self.playerClass = "Mage"
            self.inventory["spells"].append("fireball")
        elif(choice == "warrior"):
            self.attributes["strength"] += 2
            self.attributes["hp"] += 20
            self.playerClass = "Warrior"
            self.inventory["spells"].append("beserk")
        elif(choice == "healer"):
            self.attributes["toughness"] += 2
            self.attributes["mana"] += 20
            self.playerClass = "Healer"
            self.inventory["spells"].append("cure")
        else:
            print("Invalid class")
            self.chooseClass()