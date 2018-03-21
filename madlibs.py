"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("index.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Plays the game"""

    user_answer = request.args.get("play_game")

    if user_answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():

    mad_person = request.args.get("mad_person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adj")
    foods = request.args.getlist("foods")
    #print foods

    # if foods:
    #     has_foods = "Your favorite foods are:"
    # else:
    #     has_foods = ""

    temp_list = ["madlib.html","madlib2.html"]

    template = choice(temp_list)

    return render_template(template,
                           mad_person=mad_person,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           foods=foods,
                           # has_foods=has_foods
                           )



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
