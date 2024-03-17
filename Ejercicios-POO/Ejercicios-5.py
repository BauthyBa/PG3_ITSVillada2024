class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cargar(self):
        self.nombre = input("Ingrese su nombre: \n>>>")
        self.edad = int(input("Ingrese su edad: \n>>>"))

    def imprimir(self):
        print(f"Su nombre es: {self.nombre} \nSu edad es: {self.edad}")


class Empleado(Persona):
    def __init__(self, sueldo, nombre, edad):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def impuesto(self):
        if self.sueldo > 3000:
            print(f"Usted {self.nombre}, deve pagar impuestos")
        else:
            print("No deve pagar impuestos")


persona1 = Persona("", 0)
persona1.cargar()
persona1.imprimir()

empleado1 = Empleado(3100,"Bauitsta", 17)
empleado1.impuesto()
empleado1.imprimir()

        