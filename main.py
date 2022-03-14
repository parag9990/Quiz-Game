from Question_Modal import Question
from data import question_data
from Work_Brain import *

Question_Bank = []
for i in question_data:
    question_text = i['question']
    question_answer = i['correct_answer']
    new_question = Question(question_text, question_answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)
while quiz.remaining_question():
    quiz.nextQuestion()
