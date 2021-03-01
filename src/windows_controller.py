from tkinter import *


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('GBF Keyboard Controller')
        self.root.resizable(width=True, height=True)
        self.root.geometry('800x600')
        # self.root.minsize()
        # self.root.maxsize(width= ,height=)
        # self.root.icobitmap("$PATH") .ico


if __name__ == "__main__":
    # 建立主視窗
    root = Tk()
    # 常駐主視窗
    obj = Main(root)
    root.config(background="#ffffff")
    root.mainloop()
