# Ryan Kelly (rpk2kn)

from statistics import median

def is_median(func):
    for a in range(-100, 100, 5):
        for b in range(-100, 100, 5):
            for c in range(-100, 100, 5):
                if func(a, b, c) != median([a, b, c]):
                    return False
    return True
