# myMath.py
#
# Can a computer understand mathematics?
# This is an attempt to see if it can...
#

"""
        N = {'Natural Numbers': {1,2,3,5,5,6,7,8,9}},
        N0 = {'Whole Numbers': {0,1,2,3,5,5,6,7,8,9}},
        Z = {'Integers': {-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9}},
        additionSymbol = '+',
        subtractionSymbol = '-',
        multiplicationSymbol = '*',
        divisionSymbol = '/'
"""

class Arithmetic:
    def __init__(
        self,
        #N = None,
        N0 = None,
        Z = None,
        additionSymbol = None,
        subtractionSymbol = None,
        multiplicationSymbol = None,
        divisionSymbol = None
        ):

        #self.N = N
        self.N0 = N0
        self.Z = Z
        self.additionSymbol = additionSymbol
        self.subtractionSymbol = subtractionSymbol
        self.multiplicationSymbol = multiplicationSymbol
        self.divisionSymbol = divisionSymbol

    #def setN(self, N):
    #    self.N = N
    #    return

    def setN0(self, N0):
        self.N0 = N0
        return

    def setZ(self, Z):
        self.Z = Z
        return

    def setAdditionSymbol(self, aS):
        self.additionSymbol = aS
        return

    def setSubtractionSymbol(self, sS):
        self.subtractionSymbol = sS
        return

    def setMultiplicationSymbol(self, mS):
        self.multiplicationSymbol = mS
        return

    def setDivisionSymbol(self, dS):
        self.divisionSymbol = dS
        return

    # Old way, not efficient, need to use a rule
    """
    def isNatural(self, x):
        print(type(self.N))
        
        if x in self.N:
            return True
        elif isinstance(x, int) and x > 0:
            self.N.add(x)
            return True
        return False
    """
    def isNatural(self, x):
        # Cheesy, but simple, no complex test (yet)
        if isinstance(x, int):
            if x > 0:
                return True
        elif isinstance(x, float):
            return False
        elif isinstance(x, str):
            if x.isnumeric():
                if eval(x) > 0:
                    return True
        return False

    def isWhole(self, x):
        if x in self.N0:
            return True
        elif isinstance(x, int) and x > -1:
            self.N0.add(x)
            return True
        return False

    def isInteger(self, x): # Just use int class?
        if x in self.Z:
            return True
        elif isinstance(x, int):
            self.Z.add(x)
            return True
        return False

    def whatIsX(self, x):
        xIs = []
        if self.isInteger(x):
            xIs.append("INTEGER")
        if self.isWhole(x):
            xIs.append("WHOLE")
        if self.isNatural(x):
            xIs.append("NATURAL")
        return xIs

    def printAll(self):
        #print("N:  ", self.N)
        print("N0: ", self.N0)
        print("Z:  ", self.Z)
        print("Operation symbols:")
        print("   Addition:       ", self.additionSymbol)
        print("   Subtraction:    ", self.subtractionSymbol)
        print("   Multiplication: ", self.multiplicationSymbol)
        print("   Division:       ", self.divisionSymbol)

    def getAll(self):
        return {"N0": self.N0, "Z": self.Z, "additionSymbol": self.additionSymbol,
                "subtractionSymbol": self.subtractionSymbol,
                "multiplicationSymbol": self.multiplicationSymbol,
                "divisionSymbol": self.divisionSymbol}

    def simpleAdd(self, x, y):
        return x + y

    # Hokey 
    def myAdd(self, x, y):
        print("START: myAdd")
        if isinstance(x, float):
            xFloat = x
            x = int(x)
            print("Converted x: {}  to int(x): {}.".format(xFloat, x))
        elif isinstance(y, float):
            yFloat = y
            y = int(y)
            print("Converted y: {}  to int(y): {}.".format(yFloat, y))

        xArr = []
        yArr = []

        if x < 0:
            xP = x * -1
        else:
            xP = x
        
        if y < 0:
            yP = y * -1
        else:
            yP= y

        print("x & xP: ", x, xP)
        print("y & yP: ", y, yP)
        
        for i in range(0, xP):
            xArr.append(1)

        for i in range(0, yP):
            yArr.append(1)

        print(xArr)
        print(yArr)

        xLen = len(xArr)
        yLen = len(yArr)

        if x < 0:
            xLen = xLen * -1
        if y < 0:
            yLen = yLen * -1
        print("END: myAdd")
        return xLen + yLen
