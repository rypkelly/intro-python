# Ryan Kelly (rpk2kn)

name = "Ruidoquedito"
guess = ""

print("You will never win the game, for", name, "is my name.")

while guess != name:
    guess = input("Guess my name: ")
    if guess == name:
        print("No! How did you guess?")
    else:
        print("""Ha! You'll never guess!""")
