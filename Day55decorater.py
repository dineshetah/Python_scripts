# inputs = eval(input()) # eval() creates list for inputs with format:{1,2,3}

# def logging_decorator(fn):
#     def wrapper(*args):
#         print(f"You called {fn.__name__}{args}")
#         result = fn(args[0],args[1],args[2])
#         print(f"it returned: {result}")
#     return wrapper

# @logging_decorator
# def a_function(a,b,c):
#     return a * b * c
# a_function(inputs[0], inputs[1], inputs[2])


from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


# @app.route('/')
# def home():
#     return "<h1>Guess a number between 0 and 9</h1>" \
#            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)


