from flask import render_template, request
from app import app
from models.player import Player
from models.players import *
from models.game import Game
import random


@app.route("/")
def index():
    return render_template("index.html", title="Rock, Paper, Scissors!")


@app.route("/play")
def play():
    return render_template(
        "play.html",
    )


@app.route("/play", methods=["POST"])
def show_winner():
    computer_choices = ["rock", "paper", "scissors"]
    computer_option = random.choice(computer_choices)
    option = request.form.get("option")
    winner = Game.compare_choices(option, computer_option)
    player1 = Player(request.form['name'], request.form['option'])

    return render_template(
        "result.html", option=option, computer_option=computer_option, winner=winner
    )


# @app.route("/<choice1>/<choice2>")
# def play_game(choice1, choice2):

#     winner = Game.compare_choices(choice1, choice2)
#     return render_template(
#         "result.html",
#         player_list=player_list,
#         winner=winner,
#         choice1=choice1,
#         choice2=choice2,
