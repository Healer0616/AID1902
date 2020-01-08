import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()


def onButton():
    s = entry.get()  # 获取Entry的字符串
    print("您输入的是：", s)


btn = tkinter.Button(root, text="取Entry的值", command=onButton)
btn.pack()

root.mainloop()
