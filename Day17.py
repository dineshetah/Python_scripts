# How to use class function and adding methods to a Class 
class User :
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self,user) :
        user.followers += 1
        self.following +=1 
    
class car:
    def enter_race_mode():
        self.seat = 2          # example for logic understand
    my_car.enter_race_mode()
user_1 = User("001","Sonu")  # defined user function with variable 
user_2 = User("002", "Monu")
# user_1.id = "001"
# user_1.username = "Sonu"

# user_1.follow(user_2)
# #user_2.followers(user_1)

# print(user_1.followers)  # give output zero because defalut value mentioned for all attribute

# print(user_1.following)  # user_1's follwer count 
# print(user_2.following)
# print(user_2.followers) 


# # user_2 = User("002", "Monu")  # defined variable with function inside user name and id in one line code no need to last 2 line 
# user_1.id = "002"
# user_1.username = "Monu"
# # print(user_1.id)

##############################################################################
# Write a program quiz start game 
# TODo : asking the questions 
# TODO: checking if answer was correct 
# TODO: checking if we are the end of the quiz
# Here the define two variable or attributes; question number, question list in which is going to be 
# initialize  when we create a new quiz brain 
# After that create a class called QuizBrain 
# Write an __init__() method>
# Initialise the question_number to 0.
#Initialise the question_number to an input 



from question_model import Question 
from  data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
quiz.next_question()

#while # if quiz still has questions remaining 
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


