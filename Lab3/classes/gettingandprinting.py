class String:
    def getString(self):
        self.userInput = input()
    def printString(self):   
        print(self.userInput.upper())

string = String()
string.getString()
string.printString()