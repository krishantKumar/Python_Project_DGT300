
##########   IMPORTS   ##########

from tkinter import *
from tkinter import messagebox

##########   CLASS CODE   ##########
class Home:
    def __init__(self, parent):
        # setting background colour
        background_color = "#9FE7F5"

        # setting up Frame
        self.home_frame= Frame(parent, bg = background_color)

        # using place method to keep content in the frame centred
        self.home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # GUI elements
        self.heading_label = Label(self.home_frame, text="MATHS QUIZ\n"
                                   "NCEA Level 1 & 2",
                                   justify=CENTER, font=("Courier New", 32,
                                    "bold"),
                                   fg="#053F5C", bg=background_color)
        
        # using grid method to move object into different rows and columns 
        self.heading_label.grid(row=0, columnspan=3, padx=50, pady=50)

        # creating the begin quiz button
        self.begin_btn = Button(self.home_frame, text="BEGIN QUIZ",
                                font=("Arial", 24, "bold"), bg="#F7AD19",
                                fg="#053F5C", command=self.open_questions)
        
        # using grid method to move button to correct_ans location
        self.begin_btn.grid(row=1, column=0, padx=10, pady=10)

        # creating the help button
        self.help_btn = Button(self.home_frame, text="HELP",
                               font=("Arial", 24, "bold"), bg="#F7AD19",
                               fg="#053F5C", command=self.var_help)
        
        # using grid method to position help button correct_ansly
        self.help_btn.grid(row=1, column=1, padx=10, pady=10)

        self.leaderboard_button = Button(self.home_frame, text="LEADERBOARD",
                                    font=("Arial", 24, "bold"), bg="#F7AD19",
                                    fg="#053F5C", command=self.open_leaderboard
                                    )
        self.leaderboard_button.grid(row=1, column=2, padx=10, pady=10)
    
    def var_help(self):
        # Opening the help box
        get_help = Help()
        get_help.help_text.configure(text="Welcome to the Algebra Maths Quiz!\n"
                                     'To begin the quiz, press "Begin Quiz".\n'
                                     "This quiz tests you knowledge on basic\n"
                                     "Algebra skills such as solving,\n"
                                     "simplifying and expanding. NO\n"
                                     "CALCULATORS ALLOWED. These questions\n"
                                     "can be done in a book or on a paper.\n\n"
                                     "When beginning the quiz, you have three\n"
                                     "options available to choose from.\n"
                                     "Press one option and then click on the\n"
                                     '"Next Question" button. Your score\n'
                                     "will only be displayed at the end of\n"
                                     "the quiz.",                                    
                                     justify=CENTER,
                                     font=("Arial", 10, "bold"),
                                     fg="#053F5C")

    def open_leaderboard(self):
        Leaderboard()

    global leaderboard_dict
    leaderboard_dict = {}
    # # reading scores file
    try:
        with open(
            r"C:\Users\krish\Desktop\Python Project DGT300\quiz_file.txt", 'r'
            ) as read_score_file:
            scores = read_score_file.readlines()
            for line in scores:
                key, value = line.strip().split(",")
                leaderboard_dict[key] = float(value)

    except FileNotFoundError:
        print("Saving score unsuccessful (Saving file not found).") 
                
    def open_questions(self):
        # Opening the questions
        Questions()

class Leaderboard:
    def __init__(self):
        background_color = "#9FE7F5"
        self.leaderboard_box = Toplevel()
        self.leaderboard_box.geometry("640x360")
        self.leaderboard_box.state('zoomed')

        # setting up the help window background colour
        self.leaderboard_box.configure(bg=background_color)

        # setting up help frame
        self.leaderboard_frame = Frame(self.leaderboard_box, bg=background_color)

        # using place method to keep content in the frame centred
        self.leaderboard_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creating the heading for the help page using Label
        leaderboard_heading = Label(self.leaderboard_frame, text="Leaderboard", 
                             justify=CENTER, font=("Courier New", 36, "bold"), 
                             fg="#053F5C", bg=background_color)
        
        # using grid method to position heading correct_ans
        leaderboard_heading.grid(row=0, columnspan=2, padx=5, pady=5)

        # creating label for leaderboard text
        self.leaderboard_text = Text(
            self.leaderboard_frame, height=15, width=30, font=("Arial", 16), 
            padx=20, pady=20)

        # using grid method to position leaderboard text correct_ans
        self.leaderboard_text.grid(row=1, columnspan=2)

        # creating a dismiss button
        dismiss_btn = Button(self.leaderboard_frame, text="DISMISS", 
                             font=("Arial", 24, "bold"), 
                             bg="red", fg="#053F5C",
                             command=self.close_leaderboard)
        
        # using grid method to position dismiss button correct_ans
        dismiss_btn.grid(row=2, columnspan=2, pady=5, padx=5)

        # creates ordered dictionary of leaderboard
        sorted_leaderboard_dict = sorted(
            leaderboard_dict.items(), key=lambda x:x[1], reverse=True
            )
        for name, score in sorted_leaderboard_dict:
            self.leaderboard_text.insert(
                END, "Name: {}   Score: {}\n".format(name, score)
                )
        self.leaderboard_text.config(state=DISABLED)

    def close_leaderboard(self):
        # Close the leaderboard box
        self.leaderboard_box.destroy()


# Class for the help page
class Help:
    def __init__(self):
        background_color = "#9FE7F5"

        # setting up help window size
        self.help_box = Toplevel()
        self.help_box.geometry("640x360")
        # setting up the help window background colour
        self.help_box.configure(bg=background_color)

        # setting up help frame
        self.help_frame = Frame(self.help_box, bg=background_color)

        # using place method to keep content in the frame centred
        self.help_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creating the heading for the help page using Label
        help_heading = Label(self.help_frame, text="Help & Instructions", 
                             justify=CENTER, font=("Courier New", 36, "bold"), 
                             fg="#053F5C", bg=background_color)
        
        # using grid method to position heading correct_ans
        help_heading.grid(row=0, columnspan=2, padx=5, pady=5)

        # creating label for help text
        self.help_text = Label(self.help_frame, text="", justify=CENTER,
                               bg=background_color)
        # using grid method to position help text correct_ans
        self.help_text.grid(row=1, columnspan=2)

        # creating a dismiss button
        dismiss_btn = Button(self.help_frame, text="DISMISS", 
                             font=("Arial", 24, "bold"), 
                             bg="red", fg="#053F5C",
                             command=self.close_help)
        
        # using grid method to position dismiss button correct_ans
        dismiss_btn.grid(row=2, columnspan=2, pady=5, padx=5)

    def close_help(self):
        # Close the help box
        self.help_box.destroy()    
    

class Name:
    def __init__(self):
        # setting background colour
        background_color = "#9FE7F5"
        

        def submit():
            global name
            name = self.name_entry.get()
            while True:
                if len(name) <= 0:
                    root.withdraw() # close home page
                    messagebox.showerror("Name Error","Please enter a name!")
                    break
                elif  name in leaderboard_dict:
                    root.withdraw() # close home page
                    messagebox.showerror("Name Error","Name already taken!"
                                         "\nPlease enter a new name!")
                    break
                else:
                    root.withdraw() # close home page
                    self.name_box.destroy()
                    break


        
        # setting up 2nd window for name entry
        self.name_box= Toplevel()
        
        # Adjust the size and position of the window 
        self.name_box.geometry("640x360")
        self.name_box.state('zoomed')

        # setting up the window background colour
        self.name_box.configure(bg=background_color)

        self.name_frame = Frame(self.name_box, bg=background_color)
        # using place method to keep content in the frame centred
        self.name_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # GUI elements
        self.heading_name_label = Label(self.name_frame, 
                                        text="What is your name?",
                                        justify=CENTER, font=("Arial", 24,
                                                              "bold"),
                                   fg="#053F5C", bg=background_color)
        self.heading_name_label.grid(row=0, columnspan=2, padx=10, pady=10)

        self.name_entry = Entry(self.name_frame, font=("Arial", 20))
        self.name_entry.grid(row=1, columnspan=2)

        self.submit_btn = Button(self.name_frame, text="SUBMIT",
                                 justify=CENTER, font=("Arial", 14, "bold"),
                                 bg="#F7AD19", fg="#053F5C", command=submit)
        self.submit_btn.grid(row=2, columnspan=2, padx=10, pady=10)

# Class for the question pages
class Questions:
    def __init__(self):
        
        # quiz question list
        questions = [
            "Solve: 7x + 13 - 2x + 5 = 3",
            "Solve: x(4 + 6) + 25 - 8 = 7",
            "Expand and simplify: (2x - 7)(3x + 4)",
            "Expand and simplify: (4x + 8)\N{SUPERSCRIPT TWO}",
            "Solve: x\N{SUPERSCRIPT TWO} + 9x - 10 = 0",
            "Solve: 2x\N{SUPERSCRIPT TWO} + 7x - 4 = 0",
            "Solve: 5x\N{SUPERSCRIPT TWO} - 23x -10 = 0",
            "Solve: 3x\N{SUPERSCRIPT TWO} + 36x + 108",
            "Expand and simplify: (2x-7)\N{SUPERSCRIPT THREE}",
            "Expand and simplify: (3x+2)\N{SUPERSCRIPT THREE}"
        ]
        
        # quiz option list
        options = [
            ['x = 3', 'x = -3', 'x = 4', "x = -3"],
            ['x = -1', 'x = 1', 'x = 3', "x = -1"],
            ['4x\N{SUPERSCRIPT TWO}+16x-32', '6x\N{SUPERSCRIPT TWO}-13x+29',
             '6x\N{SUPERSCRIPT TWO}-13x-28', "6x\N{SUPERSCRIPT TWO}-13x-28"],
            ['16x\N{SUPERSCRIPT TWO}-64x-64', '16x\N{SUPERSCRIPT TWO}+64x-64',
             '16x\N{SUPERSCRIPT TWO}+64x+64', "16x\N{SUPERSCRIPT TWO}+64x+64"],
            ['x = 10, 1', 'x = -10,-1', 'x = -10,1', "x = -10,1"],
            ['x = 0.5,-4', 'x = -0.5,4', 'x = 0.5,4', "x = 0.5,-4"],
            ['x = -5, 2/5 ', 'x = 6', 'x = 5,-0.4', "x = 5,-0.4"],
            ['x = -6', 'x = 8', 'x = -7', "x = -6"],
            ['8x\N{SUPERSCRIPT THREE}-84x\N{SUPERSCRIPT TWO}+294x-343',
             '8x\N{SUPERSCRIPT THREE}+80x\N{SUPERSCRIPT TWO}+294x-333',
             '8x\N{SUPERSCRIPT THREE}+84x\N{SUPERSCRIPT TWO}-294x+343',
             "8x\N{SUPERSCRIPT THREE}-84x\N{SUPERSCRIPT TWO}+294x-343"],
            ['27x\N{SUPERSCRIPT THREE}-54x\N{SUPERSCRIPT TWO}+36x+8',
             '-27x\N{SUPERSCRIPT THREE}+54x\N{SUPERSCRIPT TWO}+36x+8',
             '27x\N{SUPERSCRIPT THREE}+54x\N{SUPERSCRIPT TWO}+36x+8',
             "27x\N{SUPERSCRIPT THREE}+54x\N{SUPERSCRIPT TWO}+36x+8"]
        ]

        # setting up question box
        background_color = "#9FE7F5"

        Name()

        #setting up question window size 
        self.question_box = Toplevel()
        self.question_box.geometry("640x360")
        self.question_box.state('zoomed')
        # setting up the window background colour
        self.question_box.configure(bg=background_color)

        # setting up question frame
        self.question_frame = Frame(self.question_box, bg=background_color)

        # using place method to keep content in the frame centred
        self.question_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creating heading that says "Question:"
        question_heading = Label(self.question_frame, text="Question:",
                                    justify=CENTER, 
                                    font=("Courier New", 18, "bold"),
                                    bg="#9FE7F5", fg="#053F5C")
        
        # using grid method to position question heading
        question_heading.place(relx=0.5, rely=0.05, anchor=CENTER)

        # creating white background for question
        question_label = Label(self.question_frame, height=3, width=30,
                                  bg="white",
                                  font=("Times New Roman", 24, "bold"),
                                  fg="#053F5C", wraplength=500)

        # using StringVar to manage options
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        
        # creating radiobuttons for options
        # radiobutton for option 1
        option1 = Radiobutton(self.question_frame, bg="#9FE7F5",
                                 fg="#053F5C",
                                 variable=v1,
                                 font=("Times New Roman", 24, "bold"),
                                 command=lambda: Check_Answer(option1))
        # radiobutton for option 2
        option2 = Radiobutton(self.question_frame, bg="#9FE7F5",
                                 fg="#053F5C", 
                                 variable=v2,
                                 font=("Times New Roman", 24, "bold"),
                                 command=lambda: Check_Answer(option2))
        # radiobutton for option 3
        option3 = Radiobutton(self.question_frame, bg="#9FE7F5",
                                 fg="#053F5C", 
                                 variable=v3,
                                 font=("Times New Roman", 24, "bold"),
                                 command=lambda: Check_Answer(option3))
        # creating the "next question" button
        button_next = Button(self.question_frame, text="NEXT QUESTION",
                                justify=CENTER,
                                font=("Arial", 24, "bold"), bg="#F7AD19",
                                fg="#053F5C",
                                command=lambda: display_Next_Question())

        self.question_frame.pack(fill="both", expand="true")
        # using place method to position question label 
        question_label.place(relx=0.5, rely=0.25, anchor=CENTER)

        # grid method to position options 
        option1.place(anchor=W, relx=0.1, rely=0.5)
        option2.place(anchor=W, relx=0.1, rely=0.6)
        option3.place(anchor=W, relx=0.1, rely=0.7)
        # using place method to position the next button 
        button_next.place(relx=0.5, rely=0.9, anchor=CENTER)

        index = 0
        correct_ans = 0

        # function to disable radiobuttons
        def disable_buttons(state):
            option1["state"] = state
            option2["state"] = state
            option3["state"] = state

        # function to check the selected answer
        def Check_Answer(radio):
            nonlocal correct_ans, index
            # second option is correct
            if radio["text"] == options[index][3]:
                correct_ans += 1

            index += 1
            disable_buttons("disable")

        # function to display next questions
        def display_Next_Question():
            nonlocal index, correct_ans
            global name

            # if statement to check for "Home" text in button_next
            if button_next["text"] == "Home":
                correct_ans = 0
                index = 0
                score = 0
                name = ""
                root.deiconify()  # Reopen the main Tkinter window
                self.question_box.destroy()

            # outputs the final score our of ten 
            if index == len(options):
                question_label["text"] = str(correct_ans) + " / " + '10'

                score = "{}".format(str(correct_ans))
                
                button_next["text"] = "Home"
                try:
                    with open(
                        "quiz_file.txt",
                          'a') as file:
                        file.write("\n{},{}".format(name,score))
                except FileNotFoundError:
                    print("Saving score unsuccessful (Saving file not found).")

                if correct_ans >= len(options) / 2:
                    question_label["bg"] = "green"
                else:
                    question_label["bg"] = "red"
            else:
                question_label["text"] = questions[index]

            # changes radiobuttons into a clickable state
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
root = Tk()
# Main routine
background_color = "#9FE7F5"

root.geometry("640x360")
root.state('zoomed')
root.configure(bg=background_color)
root.title("Maths Quiz")
quiz = Home(root)
root.mainloop()