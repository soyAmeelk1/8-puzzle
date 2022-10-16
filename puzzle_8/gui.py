import tkinter as tk
import tkinter.ttk as ttk
from threading import Thread
from time import sleep
from tkinter import messagebox

from puzzle_8.bfs import ok_moves, h #create ug bago na function alisdi ang possible_moves, h
import sys
sys.setrecursionlimit(10000)


def build_gui(dim):
    root = tk.Tk()
    App(root, dim).pack(side="top", fill="both", expand=True)
    root.mainloop()


class App(tk.Frame):
    def __init__(self, parent, dim, **kw):
        super().__init__(parent, **kw)
        parent.minsize(dim[0], dim[1])
        parent.title("8 puzzle problem")
        self.stop = False
        self.done = False
        self.speed = 0.5
        self.define_display_widgets()
        self.define_puzzle()
        self.start_background_task()
        messagebox.showinfo("Info", "Welcome to 8 puzzle Demo:\n\nClick on the tiles to provide input and explore !")

    def start_background_task(self):
        self.t1 = Thread(target=self.algo_update)
        self.t1.setDaemon(True)
        self.t1.start()

    