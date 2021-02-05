class MultiplyOverloaded:
    def __init__(self, a):
        self.a = a

    def __mul__(self, b):
        return self.a + b.a

case1 = MultiplyOverloaded(4)
case2 = MultiplyOverloaded(2)
print(case1*case2)