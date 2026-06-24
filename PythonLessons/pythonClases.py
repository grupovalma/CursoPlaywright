#Metodos, clases, variables, instacias variables, constructores
# Si hay un def dentro de una clase se llama Metodo
# self is mandatory for calliung variables into method.
# Instance and Class variables have whole different purpose
# This constructor name should be __init__
# New Keyboard is not required when you create object


class Calculator:
    num = 100
    #Default constructor, Segun instructor debe pulsarse ctrl + shift + F10
    def __init__(self, a, b):
        self.firstNumber = a
        self.sencondNumber = b
        print("I am called automatically wen object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Sumattion(self):
        return self.firstNumber + self.sencondNumber + Calculator.num

obj = Calculator(2, 3)
obj.getData()
print(obj.Sumattion())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Sumattion())