import random

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def determine_winner(user,computer):
    if user==computer:
        return "It's a tie!"
    elif(user =="rock"and computer =="scissors")or\
    (user =="scissors"and computer =="paper")or\
    (user =="paper"and computer =="rock"):
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    user_score=0
    computer_score=0

    while True:
        print("\nRock-Paper-Scissors Game")
        user_choice=input("Choose rock,paper,scissors(or'quit'to exit):").lower()

        if user_choice =="quit":
            print(f"Final Score ->You :{user_score},Computer:{computer_score}")
            print("Thanks for playing!")
            break
        if user_choice not in ["rock","paper","scissors"]:
            print("Invalid choice.Please try again.")
            continue
        computer_choice=get_computer_choice()
        print(f"Computer chose:{computer_choice}")

        result=determine_winner(user_choice,computer_choice)
        print(result)

        if result == "You win!":
            user_score+=1
        elif result == "You lose!":
            computer_score+=1

        print(f"Score->You:{user_score},Computer:{computer_score}")

play_game()            

    
        
        
    