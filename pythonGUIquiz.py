# Python GUI quiz project, 20/05/23
# V1

import tkinter as tk
from tkinter import *
root = tk.Tk()
class Home:
    def __init__(self, parent):
        background_color = "light blue"

        root.geometry("640x360")
        root.configure(bg = background_color)

        # setting up Frame
        self.home_frame= Frame(parent, bg = background_color)
        self.home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # GUI
        self.heading_label = Label(self.home_frame, text = "Maths Quiz",
                                      justify = CENTER, 
                                      font = "Arial 48 bold",
                                      bg = background_color)
        self.heading_label.grid(row = 0, columnspan = 2, padx = 50, pady = 50)

        self.begin_btn = Button(self.home_frame, text="Begin Quiz",
                                   font = "Arial 24 bold", bg = "dodger blue",
                                   fg = "white")
        self.begin_btn.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.help_btn = Button(self.home_frame, text = "Help",
                                  font = "Arial 24 bold", bg = "dodger blue",
                                  fg = "white", command=self.var_help)
        self.help_btn.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    def var_help(self):
        get_help = Help()
        get_help.help_text.configure(text="help goes here",
                                     justify=CENTER,
                                     font="Arial 16 bold")

class Help:
    def __init__(self):

        background_color = "light blue"

        self.help_box = Toplevel()
        self.help_box.geometry("640x360")
        self.help_box.configure(bg = background_color)
        self.help_frame = Frame(self.help_box, bg = background_color)
        self.help_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        help_heading = Label(self.help_frame, text = "Help & Instructions", 
                             justify = CENTER, font = "Arial 36 bold",
                             bg = background_color)
        help_heading.grid(row = 0, columnspan = 2, padx = 50, pady = 50)

        self.help_text = Label(self.help_frame, text="", justify=CENTER,
                               padx = 10, pady = 10, bg = background_color)
        self.help_text.grid(row = 1, columnspan=2, padx = 10, pady = 10)

    def quiz_questions(self):
        


# Main routine 
root.title("Maths Quiz")
quiz = Home(root)
root.mainloop()
