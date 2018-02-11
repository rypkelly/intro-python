# Ryan Kelly (rpk2kn)

def st_jeor(mass, height, age, sex):
    if sex == "male":
        s = 5
    else:
        s = -161
    return 10.0 * mass + 6.25 * height - 5.0 * age + s

def harris_benedict(mass, height, age, sex):
    if sex == 'male':
        return 13.7516 * mass + 5.0033 * height - 6.7550 * age + 66.4730
    else:
        return 9.5634 * mass + 1.8496 * height - 4.6756 * age + 655.0955

def revised_harris_benedict(mass, height, age, sex):
    if sex == 'male':
        return 13.397 * mass + 4.799 * height - 5.677 * age + 88.362
    else:
        return 9.247 * mass + 3.098 * height - 4.330 * age + 447.593

def katch_mcardle(mass, body_fat_percentage):
    lean_body_mass = mass - (mass * (body_fat_percentage / 100))
    return 370 + (21.6 * lean_body_mass)
