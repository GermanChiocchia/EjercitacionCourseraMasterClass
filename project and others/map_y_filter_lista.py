lista = [10, 20, 30, 40, 50]

nueva_lista = list(map(lambda x: x*2, lista))

print(nueva_lista)

otra_lista = list(filter(lambda x: x%3==0, lista))

print(otra_lista)