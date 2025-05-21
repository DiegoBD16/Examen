from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingrediente, pasos):
        self.nombre = nombre  # nombre
        self.ingrediente = ingrediente  # ingredientes
        self.pasos = pasos  # pasos

    @abstractmethod
    def mostrar(self):
        print("Ingredientes:")
        for ingrediente in self.ingrediente:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas vegetarianas
class receta_Vegetariana(receta):
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")
        return(super().mostrar())


# Clase para recetas no vegetarianas
class receta_No_Vegetariana(receta):
    def mostrar(self):
        print(f"Receta NO vegetariana: {self.nombre}")
        return(super().mostrar())


# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(ingredientes):
        for ingrediente in ingredientes:
            print(f"* {ingrediente}")

    @staticmethod
    def crear_receta(tipo_de_receta):
        recetas = []
        if receta == 1:
            receta = receta_Vegetariana()
        if receta == 2:
            receta = receta_No_Vegetariana()
        recetas.append(receta)

# Función principal
def principal():
    #Variables necesarias para la funcion crear_receta
    nombre_receta = ""
    ingredientes_receta = []
    ingredientes_pasos = []



# Ejecutar el programa
if __name__ == "__main__":
    principal()
