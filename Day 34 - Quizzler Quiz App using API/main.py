from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# FIX FOR ISSUE FROM THE CHAT - LOOK AT IT MYSELF FIRST
#
# 2 bugs w/ fixes: Rapid button click & score is off by 1 at the end
# 47 upvotes
# Teramitsu · Lecture 266 · 4 years ago
# Solutions to the 2 bugs:
#
# 1) because the score updater is inside the IF statement, it is off by 1 after the last answer since it switches to the ELSE statement and cannot update the last score. to solve this, just move the score update in front of the IF statement in the get_next_question().
#
# 2) the rapid click bug that others have mentioned. i was able to score 14 out of 10 in one round. you need to disable both buttons after any button click + else statement for the end of the quiz & restore it with the get_next_question() refresh.
#
# create methods for button_enable() & button_disable() to make it easier to read.
#
#
#
# def get_next_question(self):
#     self.canvas.config(bg="white")
#     self.score_label.config(text=f"Score: {self.quiz.score}")
#     if self.quiz.still_has_questions():
#         q_text = self.quiz.next_question()
#         self.canvas.itemconfig(self.question_text, text=q_text)
#         self.buttons_enabled()
#     else:
#         self.canvas.itemconfig(self.question_text, text="End of quiz")
#         self.buttons_disabled()
#
#
# 9 replies
#
# Steve
# 18 upvotes
# 4 years ago
# Good Idea, but you can do it in a single function passing in what state you want.
#
# def buttons_state(self,state:str):
#     self.right_button.config(state=state)
#     self.wrong_button.config(state=state)
# then call it as
#
# self.buttons_state(ACTIVE) #  ACTIVE is a tkinter string constant
# or
#
# self.buttons_state(DISABLED) #  DISABLED is a tkinter string constant