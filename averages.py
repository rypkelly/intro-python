# Ryan Kelly (rpk2kn)

def mean(a, b, c):
    return (a + b + c) / 3

def median(a, b, c):
    if a <= b <= c or a >= b >= c:
        return b
    elif b <= a <= c or b >= a >= c:
        return a
    else:
        return c

def rms(a, b, c):
    mean_square = mean(a**2, b**2, c**2)
    return mean_square ** 0.5

def middle_average(a, b, c):
    mean1 = mean(a, b, c)
    median1 = median(a, b, c)
    rms1 = rms(a, b, c)
    return median(mean1, median1, rms1)
