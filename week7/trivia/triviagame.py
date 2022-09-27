class TriviaGame():
    def __init__(self):
        self.questions = []

    def addQuestions(self,question):
        self.questions.append(question)
    
    def getQuestions(self):
        return self.questions
    
    # def multipleChoice(self):