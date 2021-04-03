daMap = [["forest", "ravine"], ["forest"], ["dungeon"], ["village"]]

playerX = 0
playerY = 0
mapSize = 10

def navigate(direction, playerX, playerY):
    if(direction == 'north' or direction == 'n'):
        if(playerY-1 < 0):
            print("Your path is blocked")
            return
        playerY -= 1
        print("You moved North successfully")
    elif(direction == 'south' or direction == 's'):
        if(playerY+1 > mapSize-1):
            print("Your path is blocked")
            return
        playerY += 1
        print("You moved South successfully")
    elif(direction == 'east' or direction == 'e'):
        if(playerX+1 > mapSize-1):
            print("Your path is blocked")
            return
        playerX += 1
        print("You moved East successfully")
    elif(direction == 'west' or direction == 'w'):
        if(playerX-1 < 0):
            print("Your path is blocked")
            return
        playerX -= 1
        print("You moved West successfully")
    else:
        print("Invalid direction")