class Wolf:
    name = "wolf"
    hp = 20
    strength = 3
    dropped_xp = 10


# implement speed to start battle
def combat_loop(enemy, player):  # add GOD MODE
    in_combat = True

    while in_combat:
        print(f'The {enemy.name} attacks for {str(enemy.strength)} damage!')
        player.attributes['hp'] -= enemy.strength

        # status printing
        print(f'Player HP: {str(player.attributes["hp"])}')
        print(f'Enemy HP: {str(enemy.hp)}')
        print()
        print("Choose an action: ")
        action = input("[ATTACK] [INVENTORY] [MAGIC] [FLEE]\n")
        print()

        if action == "ATTACK":
            enemy.hp -= player.attributes['strength']
            print("Attack successful")
            print()
        elif action == "INVENTORY":
            print("Available items: ")
            print(player.inventory["items"])
        elif action == "MAGIC":
            print("Available spells: ")
            print(player.inventory["spells"])

            spell = input("Choose a spell: ")
            if spell in player.inventory["spells"]:
                print("You use " + spell + "!")
                print()
            else:
                print("Can't use that, fool")
                print()

        elif action == "FLEE":
            print("You run away")
            print()
            break
        else:
            print("Invalid action")

        if player.attributes['hp'] <= 0:
            print("You DIED!")
            print("Try again next time, adventurer!")
            quit()
        elif enemy.hp <= 0:
            print("You won!")
            print()
            player.xp += enemy.dropped_xp
            in_combat = False
