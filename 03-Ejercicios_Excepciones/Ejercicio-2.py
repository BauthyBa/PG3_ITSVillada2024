while True:
    try:
        num1 = int(input("Ingrese el primer numero entero: "))
        num2 = int(input("Ingrese el segundo numero entero: "))
        suma = num1 + num2
        print("La suma de", num1, "y", num2, "es:", suma)

        while True:
            opcion = input("¿Desea seguir sumando valores? (1: si - 0: No): ")
            if opcion == "1":
                break
            elif opcion == "0":
                exit()
            else:
                print("Opcion invalida. Por favor, ingrese 1 para continuar o 0 para salir.")

    except ValueError:
        print("Por favor, ingrese solo numeros enteros.")
    except ZeroDivisionError:
        print("No se puede dividir por 0")