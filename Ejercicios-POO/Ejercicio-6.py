class Familia:
    def __init__(self, nombre_padre, nombre_madre, nombres_hijos):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.nombre_hijos = nombres_hijos

    #def __str__(self):
    #    print(f"El nombre del padre es {self.nombre_padre}\nEL nombre de la madre es {self.nombre_madre}")
    #    cantidad_hijos = len(self.nombre_hijos)
    #    for i in range(cantidad_hijos):
    #        print(f"El nombre del hijo {i+1} es {self.nombre_hijos[i]}")
        
    def __str__(self):
        cadena_hijos = ", ".join(self.nombre_hijos)
        return f"El nombre del padre es {self.nombre_padre}\nEL nombre de la madre es {self.nombre_madre}\nLos nombres de los hijos son {cadena_hijos}"
        

    
hijos = ["Bautista", "Luciana", "Bruno", "Enzo"]
madre = "Miriam"
padre = "Ruben"        

familia = Familia(padre, madre, hijos)
print(familia)