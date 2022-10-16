from operator import concat
import os

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")
        this.clear()
        
        this.counter = 0
        this.index = 0
        this.string = input("Введите строчку для кодирования: ")
        this.prev = this.string[0]
        this.newChar = []
        this.koeff = []
        this.CodeMessage()

    def CodeMessage(this):

        this.stringUniq = list(filter(this.UniqChar, this.string))
        this.koeff.append(str(this.index))
        this.codingStr = "".join(list(map(lambda x : "".join(x), list(zip(this.koeff, this.stringUniq)))))
        print("Кодированная строка: ", this.codingStr)
        this.Decoder()




    def UniqChar(this, x):
        this.counter = this.counter + 1 if this.prev != x else this.counter
        if this.prev == x: this.index += 1
        else: 
            this.koeff.append(str(this.index))
            this.index = 1
 
        if (this.counter, x) in this.newChar: return False
        else: 
            this.newChar.append((this.counter, x))
            this.prev = x
            return True


    def Decoder(this):
        this.decodeStr = [this.codingStr[i: i+2] for i in range(0, len(this.codingStr), 2)]
        this.decodeStr = "".join(list(map(this.DecodeProcess , this.decodeStr)))
        #this.decodeStr = "".join(list(map(lambda x: "".join([x[1] for _ in range(int(x[0]))]) , [this.codingStr[i: i+2] for i in range(0, len(this.codingStr), 2)])))
        print("Раскодированная строка: ", this.decodeStr)

    def DecodeProcess(this, x):
         return "".join([x[1] for _ in range(int(x[0]))])
        


