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
    remainingXP = 50
    

    def specialize(self, points):
        while(points > 0):
            print(str(points) + " point(s) remaining.")
            attr = input("Choose an attribute to level up: ")

            if(attr == "hp"):
                self.attributes["hp"] += 10
                points -= 1
            elif(attr == "stamina"):
                self.attributes["stamina"] += 10
                points -= 1
            elif(attr == "mana"):
                self.attributes["mana"] += 10
                points -= 1
            elif(attr == "strength"):
                self.attributes["strength"] += 1
                points -= 1
            elif(attr == "toughness"):
                self.attributes["toughness"] += 1
                points -= 1
            elif(attr == "mp"):
                self.attributes["mp"] += 1
                points -= 1
            elif(attr == "evasiveness"):
                self.attributes["evasiveness"] += 1
                points -= 1
            else:
                print("Invalid attribute choice.")
        print("No points remaining. Level up successful.")