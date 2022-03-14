import pyttsx3
# Initialise the Module(pyttsx3 - Python Text to speech Module.)
engine = pyttsx3.init()
try:
    class QuizBrain:
        def __init__(self, quesList):
            self.question_no = 0
            self.questionList = quesList
            self.score = 0

        def remaining_question(self):
            if self.question_no < len(self.questionList):
                return True
            else:
                return False

        def nextQuestion(self):
            curruntQuestion = self.questionList[self.question_no]
            self.question_no += 1
            user =  input(f'Ques{self.question_no} {curruntQuestion.text}(Enter True or False): ').title()
            self.correct_answer(user, curruntQuestion.answer)

        def correct_answer(self, user_ans, correct_ans):
            if user_ans == correct_ans:
                self.score += 1
                engine.say('You got it Right.')
                print("You got it Right.")
            else:
                engine.say('Sorry! The answer is wrong.')
                print('Sorry! The answer is wrong.')
            # engine.say(f'The Correct answer was {correct_ans}')
            print(f'The Correct answer was {correct_ans}')
            # engine.say(f'Your Current score {self.score} out of {self.question_no} question.')
            print(f'Your Current score {self.score} out of {self.question_no} question.')
            engine.runAndWait()


except:
    print("The Work Brain Module will not Working")
