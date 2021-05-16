import hero, scene, locations

Player = hero.Hero()
playerScene = scene.Scene()

print("Welcome, adventurer!")
print("Choose a class to begin the game: ")
print()
Player.chooseClass()
print()

### Game loop
while(True):        
        
    cmd = input("NEW TURN --> Enter your next move: ")
    cmdList = cmd.split()

    ### Do stuff
    if(cmd == "displayStats"):
        print("You current level is: " + str(Player.playerLevel))
        print()
        print("Your current attributes: ")
        print(Player.attributes)

    elif(cmd == "getInventory"):
        print(Player.inventory)

    elif(len(cmdList) == 2 and cmdList[0] == "move"):
        success = playerScene.navigate(cmdList[1])
        if(success):
            enterLocation = input("Would you like to explore? ")
            print()
            if(enterLocation == "yes"):
                locations.explore(scene.daMap[playerScene.playerY][playerScene.playerX], Player)

    elif(cmd == "getLocation"):
        print("You are in a " + str(scene.daMap[playerScene.playerY][playerScene.playerX]))

    elif(cmd == "help"):
        print("VALID COMMANDS")
        cmds = {"displayStats", "getInventory", "move --> usage: move + (direction)", "getLocation", "help", "exit"}
        for cmd in cmds:
            print(cmd)

    elif(cmd == "exit"):
        print("Game closed, goodbye adventurer!")
        break

    else:
        print("Invalid command.")
    print()