def ordenar(lista):
    l = len(lista)
    for i in range(l):
        for a in range(0, l-i-1):
            if lista[a] > lista[a+1]:
                lista[a], lista[a+1] = lista[a+1], lista[a]


lista_desordenada = [6, 2, 7, 23, 68, 21,674]
ordenar(lista_desordenada)
print(lista_desordenada)
