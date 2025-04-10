from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.timer = ""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",
                                 bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white",
                             highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        check_mark = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=check_mark,
            highlightbackground=THEME_COLOR,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)
        cross_mark = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=cross_mark,
            highlightbackground=THEME_COLOR,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        self.score_label.config(text=f"score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(ms=1000, func=self.get_next_question)
