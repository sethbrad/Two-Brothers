class Stringer:
    def __init__(self, myString = ''):
        self.user_string = myString

    def getString(self):
        self.user_string = input()

    def printString(self):
        print(self.user_string)

myObj = Stringer()

myObj.printString()