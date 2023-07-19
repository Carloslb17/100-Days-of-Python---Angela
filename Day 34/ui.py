from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Score Label
        self.score_label = Label(text="Score : 0 ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=3, row=0)

        # Creation of the canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, width=290, text="", font=("Ariel", 18, "bold"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, pady=(10, 40), columnspan=4)


        #Creation of the buttons
        false_logo = PhotoImage(file="images/false.png")
        self.false = Button(image=false_logo, highlightthickness=0, command=self.button_press)
        self.false.grid(column=3, row=4)

        true_logo = PhotoImage(file="images/true.png")
        self.true = Button(image=true_logo, highlightthickness=0, command= self.button_press)
        self.true.grid(column=0, row=4)

        self.next_question()
        self.window.mainloop()


    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)

    def button_press(self):
        user_answer = ""
        if self.true:
            print("True")
            return user_answer == "True"
        if self.false:
            print("False")
            return user_answer == "False"






