try:
    with open("archivo.txt", "w") as archivo:
        archivo.write(123)
except TypeError:
    print("Error: No se puede escribir un entero en el archivo.")
