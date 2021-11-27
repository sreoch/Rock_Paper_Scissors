from models.players import *
from controllers.controller import *


class Game:
    def compare_choices(choice1, choice2):
        if choice1 == choice2:
            return "It is a tie!"
        elif choice1 == "rock":
            if choice2 == "scissors":
                return "Rock beats scissors, rock wins!"
            else:
                return "Paper beats rock, paper wins!"
        elif choice1 == "paper":
            if choice2 == "rock":
                return "Paper beats rock, paper wins!"
            else:
                return "Scissors beats paper, scissors wins!"
        elif choice1 == "scissors":
            if choice2 == "paper":
                return "Scissors beats paper, scissors wins!"
            else:
                return "Rock beats scissors, rock wins!"
