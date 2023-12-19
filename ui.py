import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        self.txt = Canvas(width=40, height=30, background=THEME_COLOR, highlightthickness=0)
        self.txt.columnconfigure(0, weight=1)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.txt.grid(row=0, column=1, pady=50)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Something Text",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)

        wrong_button_img = PhotoImage(file="images/false.png")
        self.button1 = Button(image=wrong_button_img, background=THEME_COLOR, command=self.wrong_answer)
        self.button1.grid(row=2, column=1, pady=50)

        right_button_img = PhotoImage(file="images/true.png")
        self.button2 = Button(image=right_button_img, background=THEME_COLOR, command=self.right_answer)
        self.button2.grid(row=2, column=0, pady=50)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you have reach end of the quiz")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def right_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
