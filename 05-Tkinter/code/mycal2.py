import tkinter


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.entry1 = tkinter.Entry(self)  # 被加数
        self.entry2 = tkinter.Entry(self)
        self.label = tkinter.Label(self, text="+")
        self.btn = tkinter.Button(self, text="=", command=self.onCal)
        self.label_result = tkinter.Label(self)

        self.entry1.pack()
        self.label.pack()
        self.entry2.pack()
        self.btn.pack()
        self.label_result.pack()

    def onCal(self):
        s1 = self.entry1.get()
        s2 = self.entry2.get()
        try:
            s3 = int(s1) + int(s2)
            s = str(s3)
            self.label_result.config(text=s)
        except:
            self.label_result.config(text="输入有错")


root = Window()

root.mainloop()
