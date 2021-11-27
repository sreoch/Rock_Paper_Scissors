from flask import render_template, request
from app import app
from models.player import Player
from models.players import *
from models.game import Game

@app.route('/game')
def index():
    return render_template('index.html', title='Rock, Paper, Scissors!')

@app.route('/<choice1>/<choice2>')
def play_game(choice1, choice2):



    winner = Game.compare_choices(choice1, choice2)
    return render_template('result.html', player_list = player_list, winner=winner)

