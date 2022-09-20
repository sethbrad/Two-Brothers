class Wolf:
    name = "wolf"
    hp = 20
    strength = 3
    droppedXP = 10


def combat_loop(enemy, player):  # add GOD MODE
    in_combat = True

    while in_combat:
        print("The " + enemy.name + " attacks for " +
              str(enemy.strength) + " damage!")
        player.attributes['hp'] -= enemy.strength

        print("Player HP: " + str(player.attributes['hp']))
        print("Enemy HP: " + str(enemy.hp))
        print()
        print("Choose an action: ")
        action = input("[ATTACK] [INVENTORY] [MAGIC] [FLEE]")
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
            player.XP += enemy.droppedXP
            in_combat = False
