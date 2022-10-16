from operator import concat
import os

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")
        this.clear()
        this.string = "2**3*6 - 5**3 * 9 / 3**2 - 21"
        #this.string = "20-3-4"
        this.anlytic = []
        this.levelMath = {
            1: "**",
            2: "*",
            3: "/",
            4: "+",
            5: "-"
        }
        this.stringDict = {}
        this.AnalyseString()
        print(this.string)
        this.MathCalc()
        

    def AnalyseString(this):
        this.string = this.string.replace(" ", "")
        posInt = ""
        prev = ""
        for i in this.string:
            try:
                num = int(i)
                checkFlag = True
            except:
                checkFlag = False

            if checkFlag: 
                posInt += str(num)
            else: 
                if len(posInt) != 0: this.anlytic.append(posInt)
                this.anlytic.append(i)
                if i == "*" and prev == "*": 
                    this.anlytic.pop()
                    this.anlytic[len(this.anlytic)-1] = "**"

                posInt = ""
            prev = i

        this.anlytic.append(posInt)
        this.string = list(this.anlytic)
        this.whole_string = list(this.anlytic)

    def MathCalc(this):
        while len(this.string) > 1 :
            for ii in this.levelMath:
                if this.levelMath[ii] in this.string:
                    this.ConstructString(this.levelMath[ii])
                    this.Calc()
                    break

    def ConstructString(this, levelMath):
        for i in range(len(this.string)):
            if this.string[i] == levelMath:
                this.string[i] = (this.string[i-1], this.string[i], this.string[i+1])
                this.string[i-1] = (this.string[i-1], "None")
                this.string[i+1] = (this.string[i+1], "None")
                return

    def Calc(this):
        this.string = list(filter(this.Clean, this.string))
        print(this.string)
        this.string = list(map(this.Calculator, this.string))
        print(this.string)

    def Clean(this, x):
        if type(x) is tuple:
            if x[1] == "None": return False
            else: return True
        else: return True

    def Calculator(this, x):
        def CalcResult(x):
            if x[1] == "**": return str(float(x[0])**float(x[2]))
            if x[1] == "*": return str(float(x[0])*float(x[2]))
            if x[1] == "/": return str(float(x[0])/float(x[2]))
            if x[1] == "+": return str(float(x[0])+float(x[2]))
            if x[1] == "-": return str(float(x[0])-float(x[2]))

        if type(x) is tuple: return CalcResult(x)
        else: return x

