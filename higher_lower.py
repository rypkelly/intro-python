# Ryan Kelly (rpk2kn)

from random import randrange

input_num = int(input("What should the answer be? "))

if input_num == -1:
    number = randrange(101)
else:
    number = input_num

total_guesses = int(input("How many guesses? "))
guess_count = 1
guess = 0

while guess != number and guess_count <= total_guesses:
    guess = int(input("Guess a number: "))

    if guess == number:
        print("You win!")
    else:
        if guess_count == total_guesses:
            print("You lose; the number was " + str(number) + ".")
        else:
            if guess > number:
                print("The number is lower than that.")
            else:
                print("The number is higher than that.")
    guess_count += 1
