import random

class TriviaQuestion():
    def __init__(self,question,category,difficulty,correctAns,incorrectAns, id):
        self.question = question
        self.category = category
        self.difficulty = difficulty
        self.correctAns = correctAns
        self.incorrectAns = incorrectAns
        self.id = id

    def getQuestion(self):
        return self.question
    
    def getCategory(self):
        return self.category

    def getDifficulty(self):
        return self.difficulty
    
    def getCorrectAns(self):
        return self.correctAns
    
    def getInncorrectAns(self):
        return self.incorrectAns
    
    def getShuffledAnswers(self):
        answerList = self.incorrectAns
        answerList.append(self.correctAns)
        random.shuffle(answerList)
        return answerList
    
    def __str__(self):
        return f"Question: {self.question} Correct Answer: {self.correctAns}"

    def __repr__(self):
        return f"Question: {self.question} Correct Answer: {self.correctAns}"