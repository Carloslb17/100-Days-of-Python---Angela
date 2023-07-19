from flask import Flask
import random

app = Flask(__name__)

guess_number = random.randint(0, 9)


@app.route("/")
def home():
    return '<p>Hello, could you guess the number from 0 to 9?</p>' \
           '<iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/4pqm16XH2rQopZrdFU/video" width="480">'

#@app.guess_number()
#def guess_number():
    #return random.randint(0, 9)

@app.route("/<int:number>")
def next_page(number):

    if number == guess_number:
        return "<p>You won</p>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200>"
    if number > guess_number:
        return "<p>Too High</p>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200>"
    if number < guess_number:
        return "<p>Too Low</p>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200>"
if __name__ == "__main__":
    app.run(debug=True)