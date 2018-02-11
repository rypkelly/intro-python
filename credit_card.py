# Ryan Kelly (rpk2kn)

def check(card_number):
    sum1 = 0
    for digit1 in range(len(str(card_number)) - 1, -1, -2):
        sum1 += int(str(card_number)[digit1])
    remaining_digits = ""
    sum2 = 0
    for digit2 in range(len(str(card_number))-2, -1, -2):
        remaining_digits += str(2 * int(str(card_number)[digit2]))
    for digit3 in range(len(remaining_digits)):
        sum2 += int(remaining_digits[digit3])
    return (sum1 + sum2) % 10 == 0
