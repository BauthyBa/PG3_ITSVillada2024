class persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def imprimir(self):
        print("Su nombre es: ", self.nombre)

persona1 = persona("Francisco")
persona2 = persona("Bautista")
persona1.imprimir()
persona2.imprimir()
