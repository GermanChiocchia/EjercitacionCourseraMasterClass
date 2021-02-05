def divisor(a,b):
    try:
        result = str(a/b)
    except ZeroDivisionError:
        result = "can't divide by zero, please be cautelous!"
    finally:
        result +=" Thanks."
    return print(result)

a = int(input("Ingrese un valor: "))
b = int(input("Ingrese otro valor: "))
divisor(a,b)