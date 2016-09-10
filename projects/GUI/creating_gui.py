


from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text="Hey Valerie!")
        self.label.grid(row = 0, column = 1, columnspan = 2)

        ttk.Button(master, text = "In the Mood?",
                   command = self.yes).grid(row = 1, column = 1)

        ttk.Button(master, text = "I'd rather cuddle",
                   command = self.no).grid(row=1, column = 2)

    def yes(self):
            self.label.config(text="Aaaaalllrriiigght!!!")

    def no(self):
            self.label.config(text="eh, that's what Ezra is for")


def main():

    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__": main()