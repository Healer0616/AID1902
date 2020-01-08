import tkinter

root = tkinter.Tk()

entry1 = tkinter.Entry(root)  # 被加数
entry1.pack()

label = tkinter.Label(root, text="+")
label.pack()

entry2 = tkinter.Entry(root)
entry2.pack()


def onCal():
    s1 = entry1.get()
    s2 = entry2.get()
    try:
        s3 = int(s1) + int(s2)
        s = str(s3)
        label_result.config(text=s)
    except:
        label_result.config(text="输入有错")


btn = tkinter.Button(root, text="=", command=onCal)
btn.pack()

label_result = tkinter.Button(root, text="点我")
label_result.pack()

root.mainloop()
