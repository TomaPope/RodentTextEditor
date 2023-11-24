from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.filedialog import *
from tkinter.messagebox import *
import os
from tkinter import Text, Tk
from tkinter.ttk import Style, Notebook
from tklinenums import TkLineNumbers

Version = "1.0"

g = None


class Rodent():
    
    # Create New File
    def new_file(self):
        self.NewTab("Untitled", "", None)
        pass

    #Save File
    def save_file(self):
        if self.CurrentPage != None:
            if self.Addresses[self.cur] != None:
                file = open(self.Addresses[self.cur], 'w')
                file.write(self.TxtPages[self.cur].get(1.0, END))
            else:
                file = filedialog.asksaveasfilename(
                    initialfile="Unititled.txt",
                    defaultextension=".txt",
                    filetypes=[("All Files", "*.*"),
                        ("Text Documents", "*.txt")])

                if file != "":
                    self.root.title(os.path.basename(file))
                    file = open(file, "w")
                    file.write(self.TxtPages[self.cur].get(1.0, END))

    #Save As File
    def saveAS_file(self):
        if self.CurrentPage != None:
            file = filedialog.asksaveasfilename(
                initialfile="Unititled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                    ("Text Documents", "*.txt")])

            if file != "":
                self.root.title(os.path.basename(file))
                file = open(file, "w")
                file.write(self.TxtPages[self.cur].get(1.0, END))

    #Open File
    def open_file(self):
        file = askopenfilename(defaultextension=".txt",
                                file=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
        if file != "":
            # self.root.title(os.path.basename(file))
            name = os.path.basename(file)
            fileinsides = open(file, "r")
            # print(fileinsides.read())
            # print(file)
            self.NewTab(name, fileinsides.read(), file)
            # fileinsides.close()


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

    #Starts Font Option Window
    def fontoptions(self):
        pass

    def __init__(self):
        self.pages = []
        self.TxtPages = []
        self.Addresses = []
        self.CurrentPage = None
        self.cur = None
        
        #Basic Root
        self.root = Tk()
        self.root.title("Rodent")
        self.root.geometry("900x600")
        # self.tabControl = Notebook(self.root)

        #Font
        self.font_name = StringVar(self.root)
        self.font_name.set("Arial")
        self.font_size = StringVar(self.root)
        self.font_size.set("15")


        #Text Area & Scroll Bar
        self.wordwrap = False
        self.TextFrame = Frame(self.root, bg="#146")
        self.TextFrame.pack(fill=BOTH, expand=True, side=TOP)
        self.StatusBar = Frame(self.TextFrame, bg="#648", height=12)
        self.StatusBar.pack(fill=BOTH, expand=False, side=BOTTOM)
        global Version
        self.Version = Label(self.StatusBar, text=f"Version: {Version}", bg="#648", fg="#fff", padx=5)
        self.Version.pack(side=RIGHT)
        self.Position = Label(self.StatusBar, text="",bg="#648", fg="#fff", padx=5)
        self.Position.pack(side=RIGHT)

        
        
        self.TabHolder = CustomNotebook(self.TextFrame)
        self.TabHolder.pack(side=TOP, expand=True, fill=BOTH)



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
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.saveAS_file)
        self.file_menu.add_separator()
        # self.file_menu.add_command(label="Font Settings", command=self.fontoptions)
        # self.file_menu.add_separator()
        # self.file_menu.add_command(label="Exit")
        
        #Format mMenu bar
        self.format_menu.add_checkbutton(label="Word Wrap",variable=WWrap, command=self.toggleWWrap)
        # file_menu.add_command(label="Exit", command=open_file)

        self.root.after(0, self.update)

    def update(self):
        
        for i in range(len(self.pages)):
            self.pages[i].redraw()

        ray = self.TabHolder.tabs()
        self.cur = None
        if len(ray) == 0:
            self.cur = None
            self.CurrentPage = None
        for i in range(len(ray)):
            if ray[i] == self.TabHolder.select():
                self.cur = i
                self.CurrentPage = self.TxtPages[self.cur]
                
        
        if self.cur != None:
            lines = str(self.TxtPages[self.cur].index("insert").split('.')[0])
            Cols = str(self.TxtPages[self.cur].index("insert").split('.')[1])
            self.Position.config(text=f"Ln: {lines}, Col: {Cols}")
            
        # print(self.TabHolder.tabs())
        # self.linenums.redraw()
        
        
        # print(self.text_area.index("insert"))
        # lines = str(int(self.text_area.index('end-1c').split('.')[0]))
        # self.lab = Label(self.frame, text=f"Ln: {lines}")
        # self.lab.grid(row=0, column=0,stick=E)
        # print(int(self.text_area.index('end-1c').split('.')[0]))
        # self.TabHolder.forget(self.Tab1)
        self.root.after(10, self.update)

    def NewTab(self, name, words, add):
        #tabs
        self.Tab1 = Frame(self.TabHolder)
        self.TabHolder.add(self.Tab1, text=name)
        self.TabHolder.pack(expand = 1, fill=BOTH)
        
        
        
        #Line Counter
        #LineNumbers
        self.text_area = Text(self.Tab1, font=(self.font_name.get(), self.font_size.get()), wrap=NONE, bg="#733")
        self.text_area.insert(1.0, words)
        self.linenums = TkLineNumbers(self.Tab1, self.text_area, justify="center", colors=("#000", "#396"))
        self.linenums.pack(side=LEFT, fill=Y)
        
        
        #Text Area & Scroll Bars
        self.HOR_scroll_bar = Scrollbar(self.Tab1, orient=HORIZONTAL, command=self.text_area.xview)
        self.VER_scroll_bar = Scrollbar(self.Tab1, command=self.text_area.yview)
        self.HOR_scroll_bar.pack(side=BOTTOM, fill=X)
        self.VER_scroll_bar.pack(side=RIGHT, fill=Y)
        self.text_area.config(xscrollcommand=self.HOR_scroll_bar.set, yscrollcommand=self.VER_scroll_bar.set)
        self.text_area.pack(expand=True, fill=BOTH, side=LEFT)
        
        
        self.pages.append(self.linenums)
        self.TxtPages.append(self.text_area)
        self.Addresses.append(add)


class CustomNotebook(Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index
            return "break"

    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.instate(['pressed']):
            return

        element =  self.identify(event.x, event.y)
        if "close" not in element:
            # user moved the mouse off of the close button
            return

        index = self.index("@%d,%d" % (event.x, event.y))

        if self._active == index:
            global g
            g.pages.pop(index)
            g.TxtPages.pop(index)
            g.Addresses.pop(index)
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = Style()
        self.images = (
            PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])


g = Rodent()
g.root.mainloop()