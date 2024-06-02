def imprimir(ancho, alto, caracter):
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end=" ")
        print()

while True:
    ancho = int(input("Ingrese el ancho: "))
    alto = int(input("Ingrese el alto: "))
    caracter = input("Ingrese el caracter: ")   

    imprimir(ancho, alto, caracter)