from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img width=300 \
            src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess_number>")
def user_input(guess_number):
    if guess_number < random_number:
        return "<h1>The number is too low!</h1>" \
               "<img width=300 \
                src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif guess_number > random_number:
        return "<h1>The number is too high!</h1>" \
               "<img width=300 src=\
                'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1>Correct number!</h1>" \
               "<img width=300 \
                src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
