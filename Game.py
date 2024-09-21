import random

com_score = 0
player_score = 0
tie_score = 0
running = True
options = ("rock","paper","scissors") 

def checkWinner(player,computer):
    if player == computer:
        print("It's a tie!!!")

    elif player == "rock" and computer == "scissors":
        print("You Won!!!")
        return "player"
    elif player == "paper" and computer == "rock":
        print("You Won!!!")
        return "player"
    elif player == "scissors" and computer == "paper":
        print("You Won!!!") 
        return "player"   
    else:
        print("You Lose!!!")
        return "computer"
while running:
        player = None
        computer = random.choice(options)    
            
        while player not in options:
                    player = input("Enter a choice(rock,paper,scissors):-")
        
                    print(f"Player:{player}")    
                    print(f"Computer:{computer}") 

                    result = checkWinner(player, computer)
                   
                    if(result == "player"):
                        player_score += 1
                    elif(result == "computer"):
                        com_score += 1
                    else:
                        tie_score += 1
                    print("Your score: ", player_score, "computer: ", com_score, "Ties: ", tie_score)

                    if not input("Play Again?(y/n):").lower() == "y":
                        running = False

print("Thanks for playing!!!")                