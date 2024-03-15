class alumno:
    def __init__(self, nota, nombre):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        if self.nota >= 4:
            print("Nombre", self.nombre)
            print("Nota", self.nota)

    def estado(self):
        if self.nota >= 4:
            print("Regular")
        else: 
            print("Libre")

alumno1 = alumno(3, "Bautista")
alumno2 = alumno(10, "Nicolas")
alumno1.estado()
alumno2.estado()
alumno1.imprimir()
alumno2.imprimir()