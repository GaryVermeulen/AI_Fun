# myMathTester.py
#
from myMath1 import Arithmetic as arith



if __name__ == "__main__":

    arithObj = arith()

    arithObj.printAll()
    print("-----")

    ans = arithObj.myAdd(-3, 4)

    print(ans)
