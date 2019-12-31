import random
def game(string): #initiates rock paper scissors
    rng= random.randint(0,2)
    moves = ["rock","paper", "scissors"]
    computermove = moves[rng]
    print("The computer plays:", computermove)
    if str == computermove:
        print("It's a tie")
    else:
        if computermove == "rock" and str == "scissors":
            print("You lose...")
        elif computermove == "scissors" and str == "paper":
            print("You lose...")
        elif computermove == "paper" and str == "rock":
            print("You lose...")
        else:
            print("You win!")

def main():
    t = True
    play = True
    again = ""
    while t is True and play is True:
        userinput = str.strip(str.lower(input("Rock, Paper, or Scissors?")))
        while userinput != "rock" and userinput != "paper" and userinput != "scissors":
            print("Sorry, please print the correct input")
            userinput = str.strip(str.lower(input("Rock, Paper, or Scissors?")))
        if userinput != "quit":
            print("You played:", userinput)
            print(userinput)
            game(userinput)
        else:
            t = False
        if t != False:
            while again != "y" and again != "n":
                again = str.strip(str.lower(input("Would you like to play again? (y/n):")))
                if again != "y" and again != "n":
                    print("Please print the correct input")

if __name__ == '__main__':
    main()
