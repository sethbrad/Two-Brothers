import hero, daMap

Gustavo = hero.Hero()

### Game loop
while(True):
    cmd = input("Enter your next move: ")

    ### Do stuff
    if(cmd == "getStrength"):
        print(Gustavo.strength)

    elif(cmd == "move"):
        dir = input("Enter a direction: ")
        daMap.navigate(dir, daMap.playerX, daMap.playerY)