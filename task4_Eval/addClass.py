from operator import concat
import os

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")
        this.clear()
        this.string = "2**4 + 5**2 * 4 / 2**2 - 21"
        #this.stringAn = [i for i in this.string]
        this.anlytic = []
        this.levelMath = {
            1: "**",
            2: "*",
            3: "/",
            4: "+",
            5: "-"
        }
        this.AnalyseString()
        #print(this.anlytic)
        for ii in this.levelMath:
            if this.levelMath[ii] in this.string:
                print(this.levelMath[ii])
                print(this.string)
                this.currentLevelMath = this.levelMath[ii]
                this.Calc()

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

    def Calc(this):
        def Calculator(x):
            if x[1] == "**": return str(float(x[0])**float(x[2]))
            if x[1] == "*": return str(float(x[0])*float(x[2]))
            if x[1] == "/": return str(float(x[0])/float(x[2]))
            if x[1] == "+": return str(float(x[0])+float(x[2]))
            if x[1] == "-": return str(float(x[0])-float(x[2]))

        this.counter = 0
        this.newString = list(map(this.CalcGroup, this.string))
        #print(this.newString)

        i = len(this.newString)-1

        while i >=0:
            if type(this.newString[i]) is tuple:
                print(this.newString[i])
                res = Calculator(this.newString[i])
        
                for j in range(-1, 2, 1): this.newString[i-j] = "None"
                i -= 1
                this.newString[i] = str(res)
                
            else: i -= 1
                
        this.newString = list(filter(lambda x: True if x != "None" else False, this.newString))
        this.string = list(this.newString)
        print(this.newString)

    def CalcGroup(this, x):
        if x == this.currentLevelMath: y = (this.string[this.counter -1], x, this.string[this.counter +1])
        else: y = x
        this.counter += 1
        return y
                

        
    