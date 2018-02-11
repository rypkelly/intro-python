# Ryan Kelly (rpk2kn)

integer = int(input("Enter an integer: "))
copy = integer

numerals = ["M", "D", "C", "L", "X", "V", "I"]
values = [1000, 500, 100, 50, 10, 5, 1]

if 0 < integer < 4000:
    roman = ""
    for index in range(len(numerals)):
        for index2 in range(index+1, len(values)+1):
            if index2 < len(values):
                insert = values[index] - values[index2]
                if int(copy / insert) == 1 and copy < values[index] and insert != values[index2]:
                    roman += numerals[index2] + numerals[index]
                    copy -= values[index] - values[index2]
            while int(copy / values[index]) != 0:
                roman += numerals[index]
                copy -= values[index]
    print("In roman numerals,", integer, "is", roman)
else:
    print("Input must be between 1 and 3999")
