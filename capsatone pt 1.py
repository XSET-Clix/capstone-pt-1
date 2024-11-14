import random
x = random.randint(1,10)
print("Welcome to guess the number game!")
print("Guess a number from 1-10 and type the number.")
print("The Bot will tell you if the number is greater or smaller.")
print("To win you have to guess the correct number and you have as many attempts as you want.")
def game():
    turn = 0
    while True:
        turn = turn + 1
        guess = int(input("Enter a number from 1-10:"))
        if x < guess:
            print("The number is smaller.")
        elif x > guess:
            print("The number is greater")
        else:
            print("The number is correct")
            print("Attempt Number", turn)
            break
game()
choice = input("Do you want to play again yes/no:")
if choice.lower() == "yes":
    x = random.randint(1,10)
    game()
else:
    print("Thank you for playing.")