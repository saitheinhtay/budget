import random

from alembic.command import heads

print("\t\t\tCOIN FLIP GAME")
print("Guess heads or tails")

while True:
    guess = input("\nEnter your guess (heads/tails)").lower()
    flip = random.choice(["heads", "tails"])
    print(f"\nCoin shows {flip}")
    if guess == flip:
        print("You won the game ")
    else:
        print("Sorry! you guess wrong ")
    again = input("\n Play again? (yes/no)").lower()
    if not again.startswith("y"):
        print("GOODBYE!")
        break
