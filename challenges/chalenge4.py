def squad(h):
    result = h**2
    return result

def bmi(w, sh):
    result = w/sh
    return result

print('Hello,')
w=int(input('please enter your weight(in Kg): '))
h=int(input('and your height(in Meters): '))
result = bmi(w, squad(h))
print(result)