from tkinter import *

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('GBF Keyboard Controller')
        self.root.resizable(width=True, height=True)
        self.root.geometry('800x600')

if __name__ == "__main__":
    root = Tk()
    obj = Main(root)
    root.mainloop()
