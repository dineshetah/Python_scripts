# create class name Quizbrain
class QuizBrain:
    def __init__(self,q_list): # define the init function 
        self.question_number = 0                # assigned the attribute
        self.score = 0                          # assigned for score 
        self.question_list = q_list             # assigned the attribute 

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False
# Retrieve the item at the current question_number from the question_list.Use the input() function to 
# show the user the Question text and ask for the user's answer. 
    def next_question(self):
       
        current_question = self.question_list[self.question_number]
        self.question_number += 1
       
        user_answer = input(f"Q.{self.question_number}:{current_question.text}(True/False): ")
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self,user_ansewer, correct_answer):
        if user_ansewer.lower() == correct_answer.lower():
            self.score += 1 
            print("Your got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    



