### basic data types
phrase = "this is a string"
char = 'z'  #character
num1 = 4    #integer
num2 = 3.14     #float
state = True    #boolean

# if statement
if(state):
    # takes a boolean, then executes code inside
    print("if passed!")
else:
    # executes when argument is false
    print("if failed!")

# while loop
count = 5

while (count > 0):
    print(count)
    count -= 1

# for loop
for i in range(0, 5):
    print(i)

# try catch block
try:
    num = input("Enter a number: ")
    print(num)
except(KeyboardInterrupt):
    print("You broke out of the loop!")

"""
print(4 < 5)
print(10 == 10)
print(10 != 10)
print("dog" == "dog")"""