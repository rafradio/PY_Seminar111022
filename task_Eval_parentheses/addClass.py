from operator import concat
import os

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")
        this.clear()
        this.string = "(10 * (5 -2))**2 + (5 + (8**2 - 30**2 / 30))"
        this.anlytic = []
        this.levelMath = {
            1: "**",
            2: "*",
            3: "/",
            4: "+",
            5: "-"
        }
        this.AnalyseString()
        print(this.string)
        this.IsOrNotParentheses()
        
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

        if posInt != "": this.anlytic.append(posInt)
        this.string = list(this.anlytic)
        this.whole_string = list(this.anlytic)

    def IsOrNotParentheses(this):
        while len(this.string) > 1 :
            if "(" in this.whole_string:
                this.FindParentheses(0)
                this.string = this.whole_string[this.parethBegin + 1: this.parethEnd]
                this.MathCalc()
                this.string = this.whole_string[: this.parethBegin] + this.string + this.whole_string[this.parethEnd + 1:]
                this.whole_string = this.string
            else:
                this.string = this.whole_string
                this.MathCalc()
        print("Результат равен: ", this.string[0])
        

    def FindParentheses(this, begin):
        for i in range(begin, len(this.whole_string)):
            if this.whole_string[i] == "(":
                this.parethBegin = i
                if "(" in this.whole_string[this.parethBegin + 1:]: this.FindParentheses(this.parethBegin + 1)
                else:
                    for j in range(this.parethBegin + 1, len(this.whole_string)):
                        if this.whole_string[j] == ")": 
                            this.parethEnd = j
                            break
                              
                    break 
                return 

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
        this.string = list(map(this.Calculator, this.string))
        #print("Результат равен: ", this.string)

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

