import hero
import scene
import locations


# implement better string input and exception handling
def main():
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
        cmd_list = cmd.split()

        # Do stuff
        if cmd == "getStats":
            print(
                f'You are a Level {str(player.player_level)} {player.player_class}')
            print()
            print("Your current attributes: ")
            print(player.attributes)
            print(f'XP to next level-up: {player.next_level_xp - player.xp}')

        elif cmd == "getInventory":
            print(player.inventory)

        elif len(cmd_list) == 2 and cmd_list[0] in ('move', 'mv'):
            player_success = player_scene.navigate(cmd_list[1])
            if player_success:
                enter_location = input("Would you like to explore? ")
                print()
                if enter_location in ('yes', 'y'):
                    locations.explore(
                        scene.world_map[player_scene.player_y][player_scene.player_x], player)
                else:
                    print('You pass through...')

        elif cmd == "getLocation":
            loc_x = player_scene.player_x
            loc_y = player_scene.player_y
            print(
                f'You are in a {str(scene.world_map[loc_y][loc_x])}')

        elif cmd == "rest":
            player.attributes['hp'] = 100

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

# EXECUTION
if __name__ == "__main__":
    main()
