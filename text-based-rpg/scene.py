daMap = [["forest","forest","village","dungeon","forest"], 
["forest","plains","plains","plains","plains"], 
["village","plains","dungeon","plains","forest"], 
["dungeon","forest","forest","wasteland","wasteland"], 
["forest","forest","dungeon","wasteland","dragon den"]]

class Scene():
    playerX = 0
    playerY = 0
    mapSize = 5

    def navigate(self, direction):
        if(direction == 'north' or direction == 'n'):
            if(self.playerY-1 < 0):
                print("Your path is blocked")
                return False
            self.playerY -= 1
            print("You moved North to a " + daMap[self.playerY][self.playerX])
            return True
        elif(direction == 'south' or direction == 's'):
            if(self.playerY+1 > self.mapSize-1):
                print("Your path is blocked")
                return False
            self.playerY += 1
            print("You moved South to a " + daMap[self.playerY][self.playerX])
            return True
        elif(direction == 'east' or direction == 'e'):
            if(self.playerX+1 > self.mapSize-1):
                print("Your path is blocked")
                return False
            self.playerX += 1
            print("You moved East to a " + daMap[self.playerY][self.playerX])
            return True            
        elif(direction == 'west' or direction == 'w'):
            if(self.playerX-1 < 0):
                print("Your path is blocked")
                return False
            self.playerX -= 1
            print("You moved West to a " + daMap[self.playerY][self.playerX])
            return True
        else:
            print("Invalid direction")
