def desc_student(x):
    x *= 0.9
    return x

def desc_nomal(x):
    x *= 0.95
    return x

def desc_both(x):
    return desc_nomal(desc_student(x))

print(desc_both(100))