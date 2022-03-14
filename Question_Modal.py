try:
    class Question:
        def __init__(self, text, answer):
            self.text = text
            self.answer = answer
except NameError:
    print("The Question Modal of this Project will not Working.\nBecause of Name Error")
except IndexError:
    print("The Question Modal of this Project will not Working.\nBecause of Index Error")
except SyntaxError:
    print("The Question Modal of this Project will not Working.\nBecause of Syntax Error")


# For Testing the code
# q1 = Question('Ram', True)
# print(q1.text)
# print(q1.answer)
