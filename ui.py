from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_UI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=400, height=500, bg="white")
        self.canvas_text = self.canvas.create_text(200, 250, text="", width=200, fill=THEME_COLOR,
                                                   font=('italic', 15, "bold"))
        self.canvas.grid(row=1, column=1, columnspan=2, pady=20)

        green_button_img = PhotoImage(file='images/true.png')
        self.green_button = Button(image=green_button_img, command=self.green_click)
        self.green_button.grid(row=2, column=2)

        red_button_img = PhotoImage(file='images/false.png')
        self.red_button = Button(image=red_button_img, command=self.red_click)
        self.red_button.grid(row=2, column=1)

        self.score = Label(text=f"Score : {self.quiz.score}", font=('italic', 10, "bold"),
                           bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=2)

        self.create_question()

        self.window.mainloop()

    def create_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())

        else:
            self.canvas.itemconfig(self.canvas_text, text="Game Over")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def green_click(self):
        answer = self.quiz.check_answer("true")

        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.quiz.score_update(answer)
        self.window.after(1000, self.create_question)

    def red_click(self):
        answer = self.quiz.check_answer("false")

        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.quiz.score_update(answer)
        self.window.after(1000, self.create_question)
