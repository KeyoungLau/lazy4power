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

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        # To center the window on the screen.
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (615 / 2)
        y = (hs / 2) - (336 / 2)
        self.master.geometry('%dx%d+%d+%d' % (615,336,x,y))
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Command1Var = StringVar(value='Command1')
        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.top, text='Command1', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.143, rely=0.357, relwidth=0.119, relheight=0.146)

        self.Text1Font = Font(font=('宋体',9))
        self.Text1 = Text(self.top, font=self.Text1Font)
        self.Text1.place(relx=0.052, rely=0.048, relwidth=0.392, relheight=0.265)
        self.Text1.insert('1.0','')

        self.Picture1 = Canvas(self.top, takefocus=1)
        self.Picture1.place(relx=0.52, rely=0.048, relwidth=0.457, relheight=0.265)

        self.topRadioVar = StringVar()
        self.style.configure('TOption1.TRadiobutton', font=('宋体',9))
        self.Option1 = Radiobutton(self.top, text='Option1', value='Option1', variable=self.topRadioVar, style='TOption1.TRadiobutton')
        self.Option1.setValue = lambda x: self.topRadioVar.set('Option1' if x else '')
        self.Option1.value = lambda : 1 if self.topRadioVar.get() == 'Option1' else 0
        self.Option1.place(relx=0.364, rely=0.405, relwidth=0.119, relheight=0.074)

        self.style.configure('TOption2.TRadiobutton', font=('宋体',9))
        self.Option2 = Radiobutton(self.top, text='Option2', value='Option2', variable=self.topRadioVar, style='TOption2.TRadiobutton')
        self.Option2.setValue = lambda x: self.topRadioVar.set('Option2' if x else '')
        self.Option2.value = lambda : 1 if self.topRadioVar.get() == 'Option2' else 0
        self.Option2.place(relx=0.364, rely=0.548, relwidth=0.132, relheight=0.098)

        self.Check1Var = IntVar(value=0)
        self.style.configure('TCheck1.TCheckbutton', font=('宋体',9))
        self.Check1 = Checkbutton(self.top, text='Check1', variable=self.Check1Var, style='TCheck1.TCheckbutton')
        self.Check1.setValue = lambda x: self.Check1Var.set(x)
        self.Check1.value = lambda : self.Check1Var.get()
        self.Check1.place(relx=0.559, rely=0.405, relwidth=0.106, relheight=0.098)

        self.Check2Var = IntVar(value=0)
        self.style.configure('TCheck2.TCheckbutton', font=('宋体',9))
        self.Check2 = Checkbutton(self.top, text='Check2', variable=self.Check2Var, style='TCheck2.TCheckbutton')
        self.Check2.setValue = lambda x: self.Check2Var.set(x)
        self.Check2.value = lambda : self.Check2Var.get()
        self.Check2.place(relx=0.546, rely=0.571, relwidth=0.132, relheight=0.098)

        self.helloList = ['Add items in designer or code!',]
        self.helloVar = StringVar(value='Add items in designer or code!')
        self.hello = Combobox(self.top, text='Add items in designer or code!', textvariable=self.helloVar, values=self.helloList, font=('宋体',9))
        self.hello.setText = lambda x: self.helloVar.set(x)
        self.hello.text = lambda : self.helloVar.get()
        self.hello.place(relx=0.793, rely=0.405, relwidth=0.171)
        self.helloVar.trace('w', self.hello_Change)

        self.List1Var = StringVar(value='List1')
        self.List1Font = Font(font=('宋体',9))
        self.List1 = Listbox(self.top, listvariable=self.List1Var, font=self.List1Font)
        self.List1.place(relx=0.052, rely=0.571, relwidth=0.275, relheight=0.298)

        self.VScroll1 = Scrollbar(self.top, orient='vertical')
        self.VScroll1.place(relx=0.403, rely=0.048, relwidth=0.041, relheight=0.265)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def hello_Change(self, *args):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()



