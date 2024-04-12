def imprimir(ancho, alto, caracter, forma):
    if forma == 1:
        for i in range(alto):
            for j in range(ancho):
                print(caracter, end=" ")
            print()
    elif forma == 2:
        for i in range(alto):
            print(caracter * (i+1))
    else:
        print("Forma no válida")

while True:
    ancho = 0
    forma = int(input("Rectángulo - 1  Triángulo - 2 \nSeleccione la forma: "))
    if forma == 1:
        ancho = int(input("Ingrese el ancho: "))
        alto = int(input("Ingrese el alto: "))
        caracter = input("Ingrese el caracter: ")   
    else:
        alto = int(input("Ingrese el alto: "))
        caracter = input("Ingrese el caracter: ")  
    imprimir(ancho, alto, caracter, forma)
