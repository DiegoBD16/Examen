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

# Función principal
def principal():
    receta_vegetariana = receta_Vegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta_no_vegetariana = receta_No_Vegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades.imprimir_receta(receta_vegetariana)
    utilidades.imprimir_receta(receta_no_vegetariana)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ingrediente in receta_vegetariana.ingrediente:
        print(f"* {ingrediente}")
    
    print("Ingredientes de Pollo al horno:")
    for ingrediente in receta_no_vegetariana.ingrediente:
        print(f"* {ingrediente}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
