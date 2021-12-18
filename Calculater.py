from tkinter import *
window = Tk()
#Y find the way of takinig the input from the button and printing there value
#object we are found the value object input
# second we want to operand take
# how to take the second number in other position
#
label1 = Label(text = "")
label1.grid(row = 0,column = 3)
label2 = Label(text = " ")
label2.grid(row = 0,column = 5)
label3 = Label(text = "")
label3.grid(row = 0,column =4)
equal = Label(text = "=")
equal.grid(row = 0,column =6)
answer = Label(text ="Answer")
answer.grid(row =0,column = 7)
#how can i add the inputs

class first:
    value = 0

    def __init__(self,label1):
        self.label1 =label1
        self.label2 = 0
        self.code = 0
        self.r = 0

    def add2(self):
        self.label1["text"] = self.label1["text"]+ "2"
        self.r = int(self.label1["text"])
        return self.r

    def add3(self):
        self.r = self.label1["text"] =self.label1["text"] + "3"
        self.r = int(self.label1["text"])
        return self.r

    def add4(self):
        self.r = self.label1["text"] =self.label1["text"]+ "4"
        self.r = int(self.label1["text"])
        return self.r

    def add5(self):
        self.r = self.label1["text"] =self.label1["text"]+ "5"
        self.r = int(self.label1["text"])
        return self.r

    def add6(self):
        self.r = self.label1["text"] = self.label1["text"] + "6"
        self.r = int(self.label1["text"])
        return self.r

    def add7(self):
        self.r = self.label1["text"] =self.label1["text"]+ "7"
        self.r = int(self.label1["text"])
        return self.r

    def add8(self):
        self.r = self.label1["text"] = self.label1["text"]+"8"
        self.r = int(self.label1["text"])
        return self.r
    def add9(self):
        self.r = self.label1["text"] =self.label1["text"]+ "9"
        self.r = int(self.label1["text"])
        return self.r
    def add1(self):
        self.label1["text"] = self.label1["text"]+"1"
        self.r = int(self.label1["text"])
        return self.r

    def addoperand(self):
        first.value = int(self.label1["text"])
        self.label1 = label2
        label2["text"] = "+"

    def muloperand(self):
        first.value = int(self.label1["text"])
        self.label1 = label2
        label3["text"] = "x"
        self.code = 1

    def add_equal(self):
        num2 = int(self.label1["text"])
        if self.code == 0:
            add = first.value + num2
            answer["text"] = add
        elif self.code == 1:
            mul = first.value*num2
            answer["text"] =mul
            return mul
        elif self.code == 2:
            div = float(first.value/num2)
            answer["text"]= div
            return div
        elif self.code == 3:
            mod = int(first.value%num2)
            answer["text"] = mod
            return mod
        else:
            answer["text"] = 00
    def DIVIDE(self):
        first.value = int(self.label1["text"])
        self.label1 = label2
        label3["text"] = "/"
        self.code = 2
    def mod(self):
        first.value = int(self.label1["text"])
        self.label1 = label2
        label3["text"] = "%"
        self.code = 3
    def AC(self):
        answer["text"] = " "
        label1["text"] = " "
        label2["text"]= " "
        self.label1 = label1

object = first(label1 = label1)

window.minsize(width=200,height=500)
window.config(padx = 20)
button_1 = Button(text = "1",padx = 20,pady = 20,command = object.add1)
button_1.grid(row =0 ,column =0 )
button_2 = Button(text = "2",padx = 20,pady = 20,command = object.add2)
button_2.grid(row = 0,column = 1)
button_3 = Button(text = "3",padx = 20,pady = 20,command = object.add3)
button_3.grid(row = 0,column = 2)
button_4 = Button(text = "4",padx = 20,pady = 20,command = object.add4)
button_4.grid(row = 1,column = 0)
button_5 = Button(text = "5",padx = 20,pady = 20,command =object.add5)
button_5.grid(row = 1,column = 1)
button_6 = Button(text = "6",padx = 20,pady = 20,command = object.add6)
button_6.grid(row = 1,column =2)
button_7 = Button(text = "7",padx = 20,pady = 20,command = object.add7)
button_7.grid(row = 2,column = 0)
button_8 = Button(text = "8",padx = 20,pady = 20,command = object.add8)
button_8.grid(row = 2,column = 1)
button_9 = Button(text = "9",padx = 20,pady = 20,command = object.add9)
button_9.grid(row = 2,column =2)
button_addition = Button(text = "+",padx = 20,pady = 20,command = object.addoperand)
button_addition.grid(row = 3,column = 1)
button_equal = Button(text = "=",padx = 20,pady = 20,command = object.add_equal)
button_equal.grid(row = 3,column =2)
button_mul = Button(text = "x",padx = 20,pady =20,command =object.muloperand)
button_mul.grid(row = 3,column = 0)
button_AC = Button(text = "AC",padx = 20,pady = 20,command =object.AC)
button_AC.grid(row = 4,column = 2)
button_div = Button(text ="/",padx = 20,pady = 20,command = object.DIVIDE)
button_div.grid(row = 4,column = 0)
button_Rem = Button(text = "%",padx = 20,pady =20,command = object.mod)
button_Rem.grid(row = 4,column = 1)
window.mainloop()