import tkinter

root = tkinter.Tk()

label1 = tkinter.Label(root, text="aaaaa", bg="red", height=3)
label2 = tkinter.Label(root, text="bbbbb", bg="green")
label3 = tkinter.Label(root, text="ccccc", bg="blue")
label4 = tkinter.Label(root, text="ddddd", bg="orange")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2)
label4.grid(row=0, column=1, columnspan=2, sticky=tkinter.NSEW)


root.mainloop()