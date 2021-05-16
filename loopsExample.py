for i in range(0, 10):
    print(i)

###################################

counter = 9
while (counter >= 0):
    print(counter)
    counter = counter - 1 # counter -= 1 OR counter--


# Git -> add to stage, commit stage, push

while(True):
    var = input("Enter a number: ")

    if(int(var) < 0):
        break
    else:
        print("That's above zero")