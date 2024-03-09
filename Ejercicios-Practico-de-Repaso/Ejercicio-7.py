def es_step(numero):
    str_numero = str(numero)
    for i in range(len(str_numero) - 1):
        if abs(int(str_numero[i]) - int(str_numero[i+1])) != 1:
            return "El numero no es un numero step"
    return "El numero es un numero step"

while True:
    num = int(input("Ingrese un número: "))
    print(es_step(num))
    

