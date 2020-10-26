#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()


# 输出的重定向是经常需要用到的，这里介绍了一种简单实现输出重定向的方法



class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        # To center the window on the screen.
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (312 / 2)
        y = (hs / 2) - (213 / 2)
        self.master.geometry('%dx%d+%d+%d' % (312,213,x,y))
        self.createWidgets()
        sys.stdout.write = self.redirector  # 重定向关键语句1

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Command1Var = StringVar(value='Command1')
        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.top, text='Command1', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.282, rely=0.563, relwidth=0.234, relheight=0.23)

        self.Text1Font = Font(font=('宋体',9))
        self.Text1 = Text(self.top, font=self.Text1Font)
        self.Text1.place(relx=0.103, rely=0.075, relwidth=0.772, relheight=0.418)
        self.Text1.insert('1.0','')

    # 重定向关键语句，定义了一个redirector方法
    def redirector(self, inputStr):
        self.Text1.insert(INSERT, inputStr)



class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("fuck you")

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()



