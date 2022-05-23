from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(150, 125,
                                                 text="",
                                                 font=("Arial", 20, "italic"),
                                                 fill=THEME_COLOR,
                                                 width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR,
                                 fg="white", anchor="e",
                                 padx=20,
                                 font=("Arial", 17, "bold"))

        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR,
                                   command=self.check_answer_true)
        self.left_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR,
                                  command=self.check_answer_false)
        self.right_button.grid(column=1, row=2)
        self.left_button.grid(column=0, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.quiz_text, text=q_text)
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.score}")

    def check_answer_true(self):
        is_correct = self.quiz.check_answer('True')
        self.give_feedback(is_correct)

    def check_answer_false(self):
        is_correct = self.quiz.check_answer('False')
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        if self.quiz.question_number < 10:
            self.window.after(1000, self.get_next_question)
        else:
            self.window.after(1000, self.end_game)

    def end_game(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Final Score: {self.score}")
        self.canvas.itemconfig(self.quiz_text, text="Game Over")
