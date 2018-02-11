# Ryan Kelly (rpk2kn)

import os

def restock(filename, product, quantity):
    file = open(filename, "r+")
    temp = open("_temp_inventory.csv", "w+")

    found = False
    price = None

    lines = file.read().split("\n")
    for line in lines:
        element = line.split(",")
        if product in line:
            found = True
            temp.write(product + "," + str(int(element[1]) + int(quantity)) + "," + element[2] + "\n")
            quantity = int(element[1]) + int(quantity)
        elif line:
            temp.write(line + "\n")
    if not found:
        while not price:
            try:
                price = float(input("What is the price of " + product + "? "))
            except:
                continue
        temp.write(product + "," + str(quantity) + "," + str(price) + "\n")
    temp.close()
    file.close()
    os.remove(filename)
    os.rename('_temp_inventory.csv', filename)
    return quantity

def sell(filename, product, quantity):
    file = open(filename)
    temp = open("_temp_inventory.csv", "w")
    lines = file.read().split("\n")
    for line in lines:
        element = line.split(",")
        if element[0] == product:
            if quantity > float(element[1]):
                temp.write(line + "\n")
                quantity = None
            elif quantity < int(element[1]):
                temp.write(element[0] + "," + str(int(element[1]) - quantity) + "," + element[2] + "\n")
                quantity = int(element[1]) - quantity
            else:
                quantity = 0
        elif line:
            temp.write(line + "\n")
    temp.close()
    file.close()
    os.remove(filename)
    os.rename('_temp_inventory.csv', filename)
    return quantity


