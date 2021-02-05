prices = {'Peon':100,'Alfil':250,'Caballo':300,'Reina':900, 'Torre':500}
product = input('Ingrese una pieza para saber su valor')
if product in prices:
    print(prices[product],end=' $')
else:
    print('Pieza inexistente!')