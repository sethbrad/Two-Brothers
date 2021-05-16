class Wolf:
    name = "wolf"
    hp = 20
    strength = 3
    droppedXP = 10

def combatLoop(enemy, Player):
    inCombat = True

    while(inCombat):
        print("The " + enemy.name + " attacks for " + str(enemy.strength) + " damage!")
        Player.attributes['hp'] -= enemy.strength

        print("Player HP: " + str(Player.attributes['hp']))
        print("Enemy HP: " + str(enemy.hp))
        print()
        choice = input("Would you like to attack? ")

        if(choice == "yes" or choice == "y"):
            enemy.hp -= Player.attributes['strength']
            print("Attack successful")
            print()
        else:
            print("You pass")
            print()

        if(Player.attributes['hp'] <= 0):
            print("You DIED!")
            print("Try again next time, adventurer!")
            quit()
        elif(enemy.hp <= 0):
            print("You won!")
            print()
            Player.XP += enemy.droppedXP
            inCombat = False
