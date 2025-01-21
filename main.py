from question_model import Question  # this import question_model python file with Question
from  data import question_data      # this import data python file with question_data
from quiz_brain import QuizBrain     # this import quiz_brain python file with QuizBrain

question_bank = []      # stored list defined 

for question in question_data:   # using for loop each question from in question_Data 
    question_text = question["text"]     
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer) # defined new variable with Question class or (2 vairable above)

    question_bank.append(new_question) # append with blank list question bank or new question 
quiz = QuizBrain(question_bank) # define new variable with class value of question_bank in quiz brain python script
quiz.next_question()  # 

#while # if quiz still has questions remaining 
while quiz.still_has_questions(): # using while 
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")