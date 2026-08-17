import random
value=["rock","paper","scissor"]
player_score=0
computer_score=0
while True:
    player=input("enter your choice: ").lower()
    if player not in value:
        print("INVALID")
        # skip invalid input
        continue
    computer_choice=random.choice(value)
    print("computer choice",computer_choice)
    if player==computer_choice:
            print("TIE")
    elif (
        (player == "rock" and computer_choice == "scissors") or
        (player == "paper" and computer_choice== "rock") or
        (player == "scissors" and computer_choice == "paper")
    ):
        print("YOU WIN!!")
        player_score+=1
    else: 
        print("COMPUTER WIN!!")
        computer_score += 1
        print(f"Score -> You: {player_score} | Computer: {computer_score}")
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
        print("Thanks for playing!")


