prices = [100, 200, 300]
def discount(percent):
    discounted = list(map(lambda price: price*(1-percent/100),prices))
    return discounted
print(discount(10))