def esCapicua(palabra):
    palabra_capicua = 0
    l = len(palabra)
    medio_l = l//2
    for i in range(medio_l):
        if palabra[i] == palabra[-i - 1]:
            palabra_capicua += 1
        else:
            pass
    if palabra_capicua == medio_l:
        return "La palabra es un palíndromo"
    else:
        return "La palabra no es un palíndromo"

while True:
    palabra = input("Ingrese una palabra: ")
    print(esCapicua(palabra))
