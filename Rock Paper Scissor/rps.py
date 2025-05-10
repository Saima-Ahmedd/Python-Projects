import random

itemList = ["Rock", "Paper", "Scissor"]

print("\nWelcome to -- Rock, Paper and Scissor -- Game\n\n")
userChoice = input("Enter your move = Rock, Paper or Scissor = ")
compChoice = random.choice(itemList)

print(f"\nUser choice = {userChoice}, Computer choice = {compChoice}\n")

if userChoice == compChoice:
    print("Both chooses same, which means it's a tie.")


elif userChoice == "Rock":
    if compChoice == "Paper":
        print("Paper covers Rock. Hence, Computer Wins.")
    else:
        print("Rock smashes Scissor. Hence, You Win.")


elif userChoice == "Paper":
    if compChoice == "Rock":
        print("Paper covers Rock. Hence, You Wins.")
    else:
        print("Scissor cuts Paper. Hence, Computer Win.")


elif userChoice == "Scissor":
    if compChoice == "Rock":
        print("Rock smashes Scissor. Hence, Computer Wins.")
    else:
        print("Scissor cuts Paper. Hence, You Win.")



print("\n")
