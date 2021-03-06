cardNum = input('Ingrese su numero de tarjeta: ')
sumapar = 0
if len(cardNum)==16:                        #Hacemos la suma de los num impares:
    index = [x for x in range(16) if x%2==1]
    for i in index:
        sumapar = sumapar + int(cardNum[i])
                                            #Hacemos la suma de los digitos de los num pares multiplicados por 2:
    index = [x for x in range(16) if x%2==0]
    valor =[]
    for i in index:
        valor.append(int(cardNum[i])*2)     #primero duplicamos cada valor en la lista

    totalimpar = 0
    for i in range(len(valor)):
        if valor[i]>9:                      #hacemos la suma de sus digitos y la suma total
            intermedio = str(valor[i])
            mitad1 = int(intermedio[0])
            mitad2 = int(intermedio[1])
            rta = mitad1+mitad2
            totalimpar += rta
        else:
            totalimpar+=valor[i]
    total = sumapar+totalimpar                  #sumamos ambos totales y corroboramos que sea multiplo de 10

    if total%10==0:
        print('Numero de tarjeta valido!!')
    else:
        print('Numero de tarjeta invalido!!')
else:
    print('Numero de tarjeta invalido!!')