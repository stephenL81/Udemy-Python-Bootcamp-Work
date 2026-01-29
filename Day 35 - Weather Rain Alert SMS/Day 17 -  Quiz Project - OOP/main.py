import html
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create the question bank
question_bank = []
for dictionary in question_data:
    question_text = html.unescape(dictionary["question"])  # Decodes HTML entities
    question = Question(question_text, dictionary["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've completed the quiz")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
















































# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# #create the question bank. Once done  it should contain a list of question objects each initialised with a q and a
# #from the data dictionary.
#
# question_bank = []
#
# q_number = 1
# for dictionary in question_data:
#     question = Question(dictionary["question"],dictionary["correct_answer"])
#     question_bank.append(question)
#
# quiz = QuizBrain(question_bank)
#
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("\nYou've completed the quiz")
# print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")




