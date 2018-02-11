# Ryan Kelly (rpk2kn)

print("Think of a number between 1 and 100 and I\'ll guess it.")

total_guesses = int(input("How many guesses do I get? "))
guess_count = 1

range_max = 101
range_min = 0

response = ""

while guess_count <= total_guesses and response != "same" and range_max - range_min != 1:

    guess = int(range_min + (range_max - range_min) / 2)

    response = input("Is the number higher, lower, or the same as " + str(guess) + "? ")

    if response == "same":
        print("I won!")
    else:
        if response == "lower":
            range_max = guess
        else:
            range_min = guess
        if range_max - range_min == 1:
            print("Wait; how can it be both higher than " + str(range_min) + " and lower than " + str(range_max) + "?")
        else:
            if guess_count == total_guesses:
                answer = int(input("I lost; what was the answer? "))
                if answer <= range_min:
                    print("That can\'t be; you said it was higher than " + str(range_min) + "!")
                elif answer >= range_max:
                    print("That can\'t be; you said it was lower than " + str(range_max) + "!")
                else:
                    print("Well played!")

    guess_count += 1
