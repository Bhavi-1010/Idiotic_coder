# Idiotic_coder
Here's a my Python program for a Rock-Paper-Scissors game.

python
import random

def game():
    while True:
        print("\n1. Play against another player")
        print("2. Play against the computer")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            player1 = input("Enter Player 1's choice (rock/paper/scissors): ").lower()
            player2 = input("Enter Player 2's choice (rock/paper/scissors): ").lower()
            
            print(f"\nPlayer 1 chose {player1}, Player 2 chose {player2}.\n")
            
            if player1 == player2:
                print(f"Both players selected {player1}. It's a tie!")
            elif player1 == "rock":
                if player2 == "scissors":
                    print("Rock smashes scissors! Player 1 wins!")
                else:
                    print("Paper covers rock! Player 2 wins.")
            elif player1 == "paper":
                if player2 == "rock":
                    print("Paper covers rock! Player 1 wins.")
                else:
                    print("Scissors cuts paper! Player 2 wins.")
            elif player1 == "scissors":
                if player2 == "paper":
                    print("Scissors cuts paper! Player 1 wins.")
                else:
                    print("Rock smashes scissors! Player 2 wins.")
            else:
                print("Invalid input. Please enter rock, paper or scissors.")
                
        elif choice == "2":
            player = input("Enter your choice (rock/paper/scissors): ").lower()
            choices = ["rock", "paper", "scissors"]
            computer = random.choice(choices)
            
            print(f"\nYou chose {player}, computer chose {computer}.\n")
            
            if player == computer:
                print(f"Both players selected {player}. It's a tie!")
            elif player == "rock":
                if computer == "scissors":
                    print("Rock smashes scissors! You win!")
                else:
                    print("Paper covers rock! Computer wins.")
            elif player == "paper":
                if computer == "rock":
                    print("Paper covers rock! You win.")
                else:
                    print("Scissors cuts paper! Computer wins.")
            elif player == "scissors":
                if computer == "paper":
                    print("Scissors cuts paper! You win.")
                else:
                    print("Rock smashes scissors! Computer wins.")
            else:
                print("Invalid input. Please enter rock, paper or scissors.")
                
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    game()
