class Wolf:
    name = "wolf"
    hp = 20
    strength = 3
    droppedXP = 10

def combatLoop(enemy, Player): # add GOD MODE
    inCombat = True

    while(inCombat):
        print("The " + enemy.name + " attacks for " + str(enemy.strength) + " damage!")
        Player.attributes['hp'] -= enemy.strength

        print("Player HP: " + str(Player.attributes['hp']))
        print("Enemy HP: " + str(enemy.hp))
        print()
        print("Choose an action: ")
        action = input("[ATTACK] [INVENTORY] [MAGIC] [FLEE]")
        print()

        if(action == "ATTACK"):
            enemy.hp -= Player.attributes['strength']
            print("Attack successful")
            print()
        elif(action == "INVENTORY"):
            print("Available items: ")
            print(Player.inventory["items"])
        elif(action == "MAGIC"):
            print("Available spells: ")
            print(Player.inventory["spells"])

            spell = input("Choose a spell: ")
            if(spell in Player.inventory["spells"]):
                print("You use " + spell + "!")
                print()
            else:
                print("Can't use that, fool")
                print()

        elif(action == "FLEE"):
            print("You run away")
            print()
            break
        else:
           print("Invalid action")

        if(Player.attributes['hp'] <= 0):
            print("You DIED!")
            print("Try again next time, adventurer!")
            quit()
        elif(enemy.hp <= 0):
            print("You won!")
            print()
            Player.XP += enemy.droppedXP
            inCombat = False
