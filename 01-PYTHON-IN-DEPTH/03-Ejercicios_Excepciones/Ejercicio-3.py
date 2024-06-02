mes = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

try:
    numero_mes = int(input("Ingrese el numero de mes (1-12): "))
    nombre_mes = mes[numero_mes - 1]
    print("El mes correspondiente al numero", numero_mes, "es", nombre_mes)
except IndexError:
    print("El numero de mes ingresado esta fuera del rango valido (1-12)")
except ValueError:
    print("Por favor, ingrese un numero entero")