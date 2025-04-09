
class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False
    
    def alimentar(self):
        if self.alimentado:
            print(f"{self.nombre} ya estaba alimentado")
        else:
            self.alimentado = True
            print(f"{self.nombre} ha sido alimentado")
    
    def mostrar_info(self):
        estado = "Alimentado" if self.alimentado else "Hambriento"
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Estado: {estado}"

class Mamifero(Animal):
    def __init__(self, nombre, especie, pelaje):
        super().__init__(nombre, especie)
        self.pelaje = pelaje
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: Mamífero, Pelaje: {self.pelaje}"


class Ave(Animal):
    def __init__(self, nombre, especie, envergadura):
        super().__init__(nombre, especie)
        self.envergadura = envergadura
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: Ave, Envergadura: {self.envergadura}cm"
    