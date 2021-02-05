unoalcien = [x for x in range(100)]
def impar():
    impares = [x for x in unoalcien if x%2==1]
    return impares

def portres(x):
    z =[]
    for y in x:
        if y%3 == 0:
            z.append(y)
    return z
print(portres(impar()))

