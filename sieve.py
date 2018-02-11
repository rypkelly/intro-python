# Ryan Kelly (rpk2kn)

def primes(x):
    prime_list = [2]
    for y in range(3, x, 2):
        prime = True
        for z in prime_list:
            if y % z == 0:
                prime = False
        if prime:
            prime_list.append(y)
    return prime_list
