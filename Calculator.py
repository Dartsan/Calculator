import abc


class KalkulatorFactory:
    def __init__(self, userInput):
        self.sum = 0
        self.userinput = userInput

    def getNumberTypebyInput(self):
        if self.userinput.isdigit():
            print("Guat")
        else:
            if self.userinput == "+" or self.userinput == "plus" or self.userinput == "add":
                print("plus")
            elif self.userinput == "-" or self.userinput == "minus" or self.userinput == "sub":
                print("minus")
            elif self.userinput == "/" or self.userinput == ":" or self.userinput == "div":
                print("divi")
            elif self.userinput == "*" or self.userinput == "mal":
                print("mal")
            elif self.userinput == "Ergebnis" or self.userinput == "=":
                self.printErg()
            else:
                self.wrongInput()

    def printErg(self):
        print(self.sum)

    def wrongInput(self):
        print("Bitte geben Sie eine gültige Operation ein")


class Number(abc.ABC):
    def __init__(self, n1: int, n2: int, erg: float):
        self.erg = erg
        self.n1 = n1
        self.n2 = n2


class Kalkulator:

    def __init__(self, userInput):
        self.Factories = []
        self.userInput = userInput

    def createRechner(self):
        self.Factories.append(KalkulatorFactory(self.userInput))
        while len(self.Factories) > 0:
            for x in self.Factories:
                x.getNumberTypebyInput()


if __name__ == '__main__':
    print("Willkommen bei der Rechneranwendung von Kevin Herunter und Oliver Tanzer")
    k1 = Kalkulator(input())
    k1.createRechner()
