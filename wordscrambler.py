import random

print("\t\t\tWORD SCRAMBLER")
while True:
    word = input("\n Enter a word to scramble Or('quit')")
    if word.lower() == "quit":
        print("Goodbye ! ")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scramble : {"".join(letters)}")