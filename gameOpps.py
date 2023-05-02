import random

class RockPaperScissors:
    def __init__(self):
        self.gestures = {'r', 'p', 's'}

    def play(self):
        yourMove = input("type r for Rock, p for Paper and s for Scissors\n")

        while not self.validMoves(yourMove):
            print("Invalid move!")
            yourMove = input("type r for Rock, p for Paper and s for Scissors\n")

        computerMove = random.choice(list(self.gestures))

        print("You played - ", yourMove)
        print("Computer played - ", computerMove)
        if computerMove == yourMove:
            return "Match tie"
        elif computerMove == 'r':
            if yourMove == 'p':
                return "You win!"
            else:
                return "You lose!"
        elif computerMove == 'p':
            if yourMove == 's':
                return "You win!"
            else:
                return "You lose!"
        elif computerMove == 's':
            if yourMove == 'r':
                return "You win!"
            else:
                return "You lose!"

    def validMoves(self, move):
        return move in self.gestures


if __name__ == "__main__":
    rps = RockPaperScissors()
    print("Welcome to the Rock Paper Scissors!!")
    while True:
        playAgain = input("Do you want to play again?! YES/NO\n")
        if playAgain.lower() in ["yes", "y"]:
            print(rps.play())
        else:
            break
