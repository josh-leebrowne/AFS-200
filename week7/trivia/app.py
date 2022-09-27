from pickle import NONE
from flask import Flask, render_template, request
import requests
from triviagame import TriviaGame
from triviaquestion import TriviaQuestion

app = Flask(__name__)
response = requests.get(f'https://opentdb.com/api.php?amount=10&type=multiple')
data = response.json()

my_game = TriviaGame()
id = 0

for q in data['results']:
    question = q['question']
    category = q['category']
    difficulty = q['difficulty']
    correctAns = q['correct_answer']
    incorrectAns = q['incorrect_answers']

    my_questions = TriviaQuestion(question,category,difficulty,correctAns,incorrectAns, id)
    my_game.addQuestions(my_questions)
    id += 1

print(my_game.questions)


@app.route(f"/")
def hello():
    return render_template('index.html', questions = my_game.questions)

@app.route('/submit',methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        correctlyAnswered = []
        incorrectlyAnswered = []

        for question in my_game.questions:
            userAnswer = request.form[str(question.id)]
            if userAnswer == question.correctAns:
                correctlyAnswered.append(question)
            else: incorrectlyAnswered.append(question)
            
            return render_template('results.html', questions = [correctlyAnswered, incorrectlyAnswered])
    else:
        return "No Results Found"

if __name__ == "__main__":
    app.run()