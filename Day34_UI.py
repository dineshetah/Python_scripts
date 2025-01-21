from tkinter import * 
from quiz_brain import QuizBrain   # here import another file.py with clas QuizBrain 

THEME_COLOR = "#375362"         # here the menstion color theme 


class QuizInterface:     # here is mentioned class for quizinterface 

    def __init__(self, quiz_brain: QuizBrain):      # here is defined initionalized function  
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")      # HERE AFTER CHECK ANSWER CANVAS USE WHITE BACKGROUND COLOR 
        if self.quiz.still_has_questions(): # HERE CHECK THE QUESTION 
            #self.canvas.config(bg="white")  
            self.score_label.config(text=f"Score: {self.quiz.score}")  # HERE IS THE NEW SCORE LABLE AND F-STRING SELF OBJECT OR WITH NEW SCORE 
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        #is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True")) # here now set feedback function in call in is_right 

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right): # here is defined new feedback function weather check if is_right or wrong 
        if is_right:     # here if its check function right then change background color GREEN 
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red") # ELSE CHANGE BACKGRUND COLOR RED 
        self.window.after(1000, self.get_next_question) # AFTER WINDOW MILIIONS SECOND CHECK GET NEXT  QUESTION 








