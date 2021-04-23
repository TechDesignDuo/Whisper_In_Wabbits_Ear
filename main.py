from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)


@app.route('/')
def picker():
    return '<h1 style="color:blue">Sit next to the silly wabbit and whisper a number between 0 and 9 in his ear</h1>' \
           '<img src=https://media.giphy.com/media/IcifS1qG3YFlS/giphy.gif>'


@app.route('/<int:number>')
def user_guess(number):
    if number > random_num:
        return '<h1 style="color:red">TOO HIGH TRY AGAIN</h1>' \
               '<img src=https://media.giphy.com/media/2Y8Iq3xe121Ba3hUAM/giphy.gif>'
    elif number < random_num:
        return '<h1 style="color:red">TOO LOW TRY AGAIN</h1>' \
               '<img src=https://media.giphy.com/media/3ov9jRPMChw9ZzVlUk/giphy.gif>'
    else:
        return '<h1 style="color:green"> YOU GOT IT YAY</h1>' \
               '<img src=https://media.giphy.com/media/pfwC4n3pbS5UY/giphy.gif>' \
               '<img src=https://media.giphy.com/media/23xN9cYQSKwFy/giphy.gif>'


if __name__ == "__main__":
    app.run(debug=True)