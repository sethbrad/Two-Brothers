import hero
import scene
import locations

player = hero.Hero()
player_scene = scene.Scene()

print("Welcome, adventurer!")
print("Choose a class to begin the game: ")
print()
player.choose_class()
print()

# Game loop
while True:

    print("# # # # # # # #")
    cmd = input("NEW TURN --> Enter your next move: ")
    cmdList = cmd.split()

    # Do stuff
    if cmd == "getStats":
        print("You are a Level " + str(player.player_level) +
              " " + player.player_class)
        print()
        print("Your current attributes: ")
        print(player.attributes)

    elif cmd == "getInventory":
        print(player.inventory)

    elif len(cmdList) == 2 and cmdList[0] == "move":
        SUCCESS = player_scene.navigate(cmdList[1])
        if SUCCESS:
            enterLocation = input("Would you like to explore? ")
            print()
            if enterLocation == "yes":
                locations.explore(
                    scene.daMap[player_scene.playerY][player_scene.playerX], player)

    elif cmd == "getLocation":
        print("You are in a " +
              str(scene.daMap[player_scene.playerY][player_scene.playerX]))

    elif cmd == "help":
        print("VALID COMMANDS")
        cmds = {
            "getStats",
            "getInventory",
            "move --> usage: move + (direction)",
            "getLocation",
            "help",
            "exit"}
        for cmd in cmds:
            print(cmd)

    elif cmd == "exit":
        print("Game closed, goodbye adventurer!")
        break

    else:
        print("Invalid command.")
    print()
