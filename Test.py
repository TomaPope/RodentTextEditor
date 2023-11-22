from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.filedialog import *
from tkinter.messagebox import *
import os
from tkinter import Text, Tk
from tkinter.ttk import Style
from tklinenums import TkLineNumbers

public_file = None

Version = "1.0"


class Rodent():
    #Create New File
    def new_file(self):
            self.root.title("Untitled - Rodent")
            global public_file
            if public_file != None:
                self.save_file()
            self.text_area.delete(1.0, END)
            public_file = None
    #Save File
    def save_file(self):
            global public_file
            if public_file == None:
                file = filedialog.asksaveasfilename(
                    initialfile="Unititled.txt",
                    defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                                ("Text Documents", "*.txt")])

                if file is None:
                    return
                else:
                    try:
                        self.root.title(os.path.basename(file))
                        file = open(file, "w")
                        file.write(self.text_area.get(1.0, END))
                    except Exception:
                        print("Couldn't save")
                    finally:
                        file.close()
            else:
                file = open(public_file, "w")
                file.write(self.text_area.get(1.0, END))
    #Open File
    def open_file(self):
        global public_file
        if public_file != None:
            self.save_file()
        file = askopenfilename(defaultextension=".txt",
                                file=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
        try:
            self.root.title(os.path.basename(file))
            public_file = file
            self.text_area.delete(1.0, END)
            file = open(file, "r")
            self.text_area.insert(1.0, file.read())
        except EXCEPTION:
                print("error")
        finally:
            file.close()


        # def update():
        #     txt = text_area.get(1.0, END)
        #     print(len(txt))
    #toggles Word Wrap
    def toggleWWrap(self):
        self.wordwrap = not self.wordwrap
        if self.wordwrap:
            self.text_area.config(wrap=WORD)
        else:
            self.text_area.config(wrap=NONE)


    def __init__(self):
        #Basic Root
        self.root = Tk()
        self.root.title("Untitled - Rodent")
        self.root.geometry("500x500")

        #Font
        self.font_name = StringVar(self.root)
        self.font_name.set("Arial")
        self.font_size = StringVar(self.root)
        self.font_size.set("15")







        #Text Area & Scroll Bar
        self.wordwrap = False
        #Frame For Text
        self.TextFrame = Frame(self.root, bg="#146")
        self.TextFrame.pack(fill=BOTH, expand=True, side=TOP)
        # Status Bar
        self.StatusBar = Frame(self.TextFrame, bg="#648", height=12)
        self.StatusBar.pack(fill=BOTH, expand=False, side=BOTTOM)
        global Version
        self.Version = Label(self.StatusBar, text=f"Version: {Version}", bg="#648", fg="#fff", padx=5)
        self.Version.pack(side=RIGHT)
        self.Position = Label(self.StatusBar, text="112",bg="#648", fg="#fff", padx=5)
        self.Position.pack(side=RIGHT)
        # self.TextFrame.grid_columnconfigure((0,1), weight=1)

        #Line Counter
        #LineNumbers
        self.text_area = Text(self.TextFrame, font=(self.font_name.get(), self.font_size.get()), wrap=NONE, bg="#733")
        self.linenums = TkLineNumbers(self.TextFrame, self.text_area, justify="center", colors=("#000", "#396"))
        self.linenums.pack(side=LEFT, fill=Y)
        
        # self.text_area.bind("<<Modified>>", lambda event: self.TextFrame.after_idle(self.linenums.redraw), add=True)
        
        # self.Other = Label(self.TextFrame, text="116", bg="#528")
        # self.Other.pack(side=LEFT)
        # self.Count = Label(self.TextFrame, text="112", bg="#aaa")
        # self.Count.pack(side=LEFT)
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_columnconfigure(0, weight=1)
        
        
        # #Text Area & Scroll Bars
        self.style = Style()
        self.style.theme_use('classic')
        self.style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")
        self.HOR_scroll_bar = Scrollbar(self.TextFrame, orient=HORIZONTAL, command=self.text_area.xview, activebackground="#214")
        self.VER_scroll_bar = Scrollbar(self.TextFrame, command=self.text_area.yview)
        self.HOR_scroll_bar.pack(side=BOTTOM, fill=X)
        self.VER_scroll_bar.pack(side=RIGHT, fill=Y)
        self.text_area.config(xscrollcommand=self.HOR_scroll_bar.set, yscrollcommand=self.VER_scroll_bar.set)
        self.text_area.pack(expand=True, fill=BOTH, side=LEFT)
        
        
        
        # self.lab1 = Label(self.test, text="1", bg="#ffffff")
        # self.lab1.pack(side=BOTTOM)
        




        #FOOTBAR
        # self.frame = Frame(self.root, bg="#857")
        # self.frame.grid(sticky=N + E + S + W)
        # self.frame.pack(fill=BOTH, expand=True)
        # self.lab1 = Label(self.frame, text="1", bg="#ffffff")
        
        # self.lab1 = Label(self.frame, text="1", bg="#ffffff", borderwidth=1, relief=GROOVE, padx= 20)
        # self.frame.columnconfigure(0, weight=1)
        # self.lab1.grid(row=0, column=7, stick=E + S) 

        #Menu Bar
        WWrap = BooleanVar()
        WWrap.set(self.wordwrap)
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.format_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        #File Menu Bar
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        #Format mMenu bar
        self.format_menu.add_checkbutton(label="Word Wrap",variable=WWrap, command=self.toggleWWrap)
        # file_menu.add_command(label="Exit", command=open_file)

        self.root.after(0, self.update)
        self.root.mainloop()
        # print("start")

    def update(self):
        self.linenums.redraw()
        # print(self.text_area.index("insert"))
        # lines = str(int(self.text_area.index('end-1c').split('.')[0]))
        lines = str(self.text_area.index("insert").split('.')[0])
        Cols = str(self.text_area.index("insert").split('.')[1])
        self.Position.config(text=f"Ln: {lines}, Col: {Cols}")
        # self.lab = Label(self.frame, text=f"Ln: {lines}")
        # self.lab.grid(row=0, column=0,stick=E)
        # print(int(self.text_area.index('end-1c').split('.')[0]))
        self.root.after(10, self.update)

Rodent()