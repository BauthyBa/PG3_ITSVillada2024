def bisiesto(ano):
    if ano % 4 == 0:
        return "EL ano es bisiesto"
    else:
        return "El ano no es bisiesto"

while True:
    ano = int(input("Ingrese un ano: "))
    print(bisiesto(ano))