import random

print(" Welcome to the Rock Paper Scissors!! ")
gestures = {'r', 'p', 's'}

def game ():
    yourMove = input("  type r for Rock , p for Paper and s for Scissors \n")

    while not validMoves(yourMove) :
        print("Invalid move!")
        yourMove = input("  type r for Rock , p for Paper and s for Scissors \n")

    computerMove = random.choice(list(gestures))

    print ("You played - " , yourMove)
    print ("Computer played - " , computerMove)
    if computerMove == yourMove:
        return " Match tie "
    
    else:
        if computerMove == 'r' :
            if yourMove == 'p':
                return " You win! "
            else:
                return " You lose! "
        elif computerMove == 'p' :
            if yourMove == 's':
                return " You win! "
            else:
                return " You lose! "
        else:
            if yourMove == 'r':
                return " You win! "
            else:
                return " You lose! "

    return " Game played! "

def validMoves (move):
    return move in gestures 


if __name__ == "__main__":

    while True :

        # print(" Do you want to play again?! YES / NO ")
        playAgain = input("  Do you want to play again?! YES / NO  \n")
        if playAgain == "yes" or playAgain == "Yes" or playAgain == "YES":
            print(game())
        else:
            break
