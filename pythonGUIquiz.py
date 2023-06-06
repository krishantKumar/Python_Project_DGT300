# Python GUI quiz project, 20/05/23
# V1

import tkinter as tk
from tkinter import *
from tkinter import StringVar

# Class for the home page
"""Class Home creates the Home page with Begin Quiz button and Help button"""
class Home:
    def __init__(self, parent):
        # setting background colour
        background_color = "#B3E0EE"

        # setting up Frame
        self.home_frame= Frame(parent, bg = background_color)

        # using place method to keep content in the frame centred
        self.home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # GUI elements
        self.heading_label = Label(self.home_frame, text="MATHS QUIZ",
                                   justify=CENTER, font="Arial 48 bold",
                                   bg=background_color)
        
        # using grid method to move object into different rows and columns 
        self.heading_label.grid(row=0, columnspan=2, padx=50, pady=50)

        # creating the begin quiz button
        self.begin_btn = Button(self.home_frame, text="BEGIN QUIZ",
                                font="Arial 24 bold", bg="#0196C1",
                                fg="white", command=self.open_questions)
        
        # using grid method to move button to correct location
        self.begin_btn.grid(row=1, column=0, padx=10, pady=10)

        # creating the help button
        self.help_btn = Button(self.home_frame, text="HELP",
                               font="Arial 24 bold", bg="#0196C1",
                               fg="white", command=self.var_help)
        
        # using grid method to position help button correctly
        self.help_btn.grid(row=1, column=1, padx=10, pady=10)
    
    def var_help(self):
        # Opening the help box
        get_help = Help()
        get_help.help_text.configure(text="help goes here",
                                     justify=CENTER,
                                     font="Arial 16 bold")
        
    def open_questions(self):
        # Opening the questions
        questions = Questions()

# Class for the help page
class Help:
    def __init__(self):
        background_color = "#B3E0EE"

        # setting up help window size
        self.help_box = Toplevel()
        self.help_box.geometry("640x360")
        self.help_box.configure(bg=background_color)

        # setting up help frame
        self.help_frame = Frame(self.help_box, bg=background_color)

        # using place method to keep content in the frame centred
        self.help_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creating the heading for the help page using Label
        help_heading = Label(self.help_frame, text="Help & Instructions", 
                             justify=CENTER, font="Arial 36 bold",
                             bg=background_color)
        
        # using grid method to position heading correctly
        help_heading.grid(row=0, columnspan=2, padx=50, pady=50)

        # creating label for help text
        self.help_text = Label(self.help_frame, text="", justify=CENTER,
                               padx=10, pady=10, bg=background_color)
        self.help_text.grid(row=1, columnspan=2, padx=10, pady=10)

        # creating a dismiss button
        dismiss_btn = Button(self.help_frame, text="DISMISS", 
                             font="Arial 24 bold", padx=2, pady=2, bg="red", 
                             fg="white", command=self.close_help)
        
        # using grid method to position dismiss button correctly
        dismiss_btn.grid(row=2, columnspan=2, pady=10)

    def close_help(self):
        # Close the help box
        self.help_box.destroy()

# Class for the question pages
class Questions:
    def __init__(self):
        
        # quiz question list
        questions = [
            "Solve: 7x + 13 - 2x + 5 = 3",
            "Solve: x(4 + 6) + 25 - 8 = 7",
            "Expand and simplify: (2x - 7)(3x + 4)",
            "Expand and simplify: (4x + 8)^2",
            "Solve: x^2 + 9x - 10 = 0",
            "Solve: 2x^2 + 7x - 4 = 0",
            "Solve: 2^(x-3) = 4",
            "Solve: 9^(2x+4) = 27^(x+5)",
            "Expand and simplify: (2x-7)^3",
            "Expand and simplify: (3x+2)^3"
        ]
        
        # quiz option list
        options = [
            ['x = 3', 'x = -3', 'x = 4', 'x = -3'],
            ['x = -1', 'x = 1', 'x = 3', 'x = -1'],
            ['4x^2+16x-32', '6x^2-13x+29', '6x^2-13x-28', '6x^2-13x-28'],
            ['4x^2-5x-16', '4x^2+5x-16', '4x^2+5x+16', '4x^2+5x+16'],
            ['x = 10, 1', 'x = -10,-1', 'x = -10,1', 'x = -10,1'],
            ['x = 0.5,-4', 'x = -0.5,4', 'x = 0.5,4', 'x = 0.5,-4'],
            ['x = -5', 'x = 6', 'x = 5', 'x = 5'],
            ['x = 7', 'x = 8', 'x = -7', 'x = 7'],
            ['8x^3-84x^2+294x-343', '8x^3+80x^2+294x-333',
             '8x^3+84x^2-294x+343', '8x^3-84x^2+294x-343'],
            ['27x^3-54x^2+36x+8', '-27x^3+54x^2+36x+8',
             '27x^3+54x^2+36x+8', '27x^3+54x^2+36x+8']
        ]

        # setting up question box
        background_color = "#B3E0EE"

        self.question_box = Toplevel()
        self.question_box.geometry("640x360")
        self.question_box.configure(bg=background_color)

        # setting up question frame
        self.question_frame = Frame(self.question_box, bg=background_color)

        # using place method to keep content in the frame centred
        self.question_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creating heading that says "Question:"
        question_heading = tk.Label(self.question_frame, text="Question:",
                                    justify=CENTER, 
                                    font="Arial 18 bold", bg="#B3E0EE")
        
        # using grid method to position question heading
        question_heading.grid(row=0, column=0)

        # creating white background for question
        question_label = tk.Label(self.question_frame, height=3, width=30,
                                  bg="white", font="Arial 24 bold",
                                  wraplength=500)

        # using StringVar to manage options
        v1 = StringVar(self.question_frame)
        v2 = StringVar(self.question_frame)
        v3 = StringVar(self.question_frame)
        
        # creating radiobuttons for options
        option1 = tk.Radiobutton(self.question_frame, bg="#B3E0EE", 
                                 variable=v1, font="Arial 18 bold",
                                 command=lambda: checkAnswer(option1))
        option2 = tk.Radiobutton(self.question_frame, bg="#B3E0EE", 
                                 variable=v2, font="Arial 18 bold",
                                 command=lambda: checkAnswer(option2))
        option3 = tk.Radiobutton(self.question_frame, bg="#B3E0EE", 
                                 variable=v3, font="Arial 18 bold",
                                 command=lambda: checkAnswer(option3))
        # creating the "next question" button
        button_next = tk.Button(self.question_frame, text="NEXT QUESTION",
                                justify=CENTER,
                                bg="#0196C1", fg="white", 
                                font="Arial 24 bold",
                                command=lambda: display_Next_Question())


        self.question_frame.pack(fill="both", expand="true")
        question_label.grid(row=1, column=0)

        # grid method to position options 
        option1.grid(sticky=W, row=2, column=0)
        option2.grid(sticky=W, row=3, column=0)
        option3.grid(sticky=W, row=4, column=0)

        button_next.grid(row=6, column=0)

        index = 0
        correct = 0

        # function to disable radiobuttons
        def disable_buttons(state):
            option1["state"] = state
            option2["state"] = state
            option3["state"] = state

        # function to check the selected answer
        def checkAnswer(radio):
            nonlocal correct, index

            # second option is correct
            if radio["text"] == options[index][3]:
                correct += 1

            index += 1
            disable_buttons("disable")

        # function to display next questions
        def display_Next_Question():
            nonlocal index, correct

            # if statement to check for "Home" text in button_next
            if button_next["text"] == "Home":
                correct = 0
                index = 0
                self.question_box.destroy()

            # outputs the final score our of ten 
            if index == len(options):
                question_label["text"] = str(correct) + " / " + str(len(options))
                button_next["text"] = "Home"
                if correct >= len(options) / 2:
                    question_label["bg"] = "green"
                else:
                    question_label["bg"] = "red"
            else:
                question_label["text"] = questions[index]

            
            disable_buttons("normal")
            opts = options[index]
            option1["text"] = opts[0]
            option2["text"] = opts[1]
            option3["text"] = opts[2]
            v1.set(opts[0])
            v2.set(opts[1])
            v3.set(opts[2])

            if index == len(options) - 1:
                button_next["text"] = "Check your results"

        display_Next_Question()

# Creating main window
root = tk.Tk()
# Main routine
background_color = "#B3E0EE"

root.geometry("640x360")
root.configure(bg=background_color)
root.title("Maths Quiz")
quiz = Home(root)
root.mainloop()
