def busqueda(lista, elemento_buscado):
    try:
        posicion = lista.index(elemento_buscado)
        return posicion
    except ValueError:
        return "El número no está en la lista"

numeros = [7, 89, 0, 34, 1]

while True:
    elemento = int(input("Ingrese el número a buscar: "))
    print(busqueda(numeros, elemento))
