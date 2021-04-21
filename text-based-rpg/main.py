import hero, scene, locations

Player = hero.Hero()
playerScene = scene.Scene()

### Game loop
while(True):
    cmd = input("Enter your next move: ")

    ### Do stuff
    if(cmd == "displayStats"):
        print(Player.attributes)

    elif(cmd == "move"):
        dir = input("Enter a direction: ")
        success = playerScene.navigate(dir)
        if(success):
            enterLocation = input("Would you like to explore? ")
            if(enterLocation == "yes"):
                locations.explore(scene.daMap[playerScene.playerY][playerScene.playerX])

    elif(cmd == "getLocation"):
        print("You are in a " + str(scene.daMap[playerScene.playerY][playerScene.playerX]))

    elif(cmd == "exit"):
        print("Game closed, goodbye adventurer!")
        break

    else:
        print("Invalid command.")
    print()