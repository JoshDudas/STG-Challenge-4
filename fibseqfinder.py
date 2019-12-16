from numtostringconverter import NumberToString

class FibValue:

    def getFibNumValue(self, FibNumber):
        firstNumber = 0
        secondNumber = 0
        fibNumberValue = 0

        if FibNumber > 0:
            fibNumberValue = 1
            for count in range(1, FibNumber):
                firstNumber = fibNumberValue
                fibNumberValue = fibNumberValue + secondNumber
                secondNumber = firstNumber
        print(fibNumberValue)
        return fibNumberValue

if __name__ == '__main__':
    fibNumberFinder = FibValue()
    fibNumber = fibNumberFinder.getFibNumValue(34)
