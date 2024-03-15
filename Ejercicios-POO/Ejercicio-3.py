class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor(self):
        bigger = max(self.lado1, self.lado2, self.lado3)
        print("El mayor es:", bigger)

    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Es equilatero")
        else:
            print("No es equilatero")

ejemplo1 = Triangulo(3,4,5)
ejemplo2 = Triangulo(3,3,3)
ejemplo1.mayor()
ejemplo2.equilatero()