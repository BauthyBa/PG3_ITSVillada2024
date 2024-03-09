def vocales(palabra):
    vocales = ["a", 'e', 'i', 'o','u']
    cant_vocales = 0
    l = len(palabra)
    for i in range(l):
        if palabra[i] in vocales:
            cant_vocales += 1
        else:
            pass
    return "La palabra tiene ", cant_vocales, " Vocales"

while True:
    palabra = input("Ingrese una palabra: ")
    print(vocales(palabra))
