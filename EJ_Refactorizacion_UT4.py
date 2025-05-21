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
    pregunta = 0
    recetas = []
    listas_de_ingredientes = []
    while pregunta != 4:
        pregunta = int(input("¿Que quieres hacer? 1: crear receta, 2: mostrar receta, 3: mostrar ingredientes, 4: finalizar"))
        if pregunta == 1:
            crear_receta(recetas, listas_de_ingredientes)
        elif pregunta == 2:
            receta = int(input("Que receta quieres imprimir?: "))
            utilidades.imprimir_receta(recetas[receta])
        elif pregunta == 3:
            receta = int(input("¿De que receta quieres los ingredientes?: "))
            utilidades.mostrar_lista_ingredientes(listas_de_ingredientes[receta])

def crear_receta(recetas, listas_de_ingredientes):
    ingredientes_receta = []
    receta_pasos = []
    tipo_de_receta = int(input("¿Escribe 1 para una receta vegetariana o 2 para una receta no vegetariana: "))
    nombre_receta = str(input("¿Nombre?: "))

            #Pido los ingredientes
    numero_ingredientes = int(input("¿Cuantos ingredientes llevara?: "))
    for i in range(numero_ingredientes):
        ingrediente = str(input("¿Ingrediente?: "))
        ingredientes_receta.append(ingrediente)

            #Pido los pasos
    numero_pasos = int(input("¿en cuantos pasos se hace?: "))
    for p in range(numero_pasos):
        paso = str(input("¿Paso?: "))
        receta_pasos.append(paso)
            #Creo la receta y la guardo en la lista "recetas", lo mismo con los ingredientes que los guardo en "lista_de_ingredientes"

    if tipo_de_receta == 1:
        receta = receta_Vegetariana(nombre_receta, ingredientes_receta, receta_pasos)
    elif tipo_de_receta == 2:
        receta = receta_No_Vegetariana(nombre_receta, ingredientes_receta, receta_pasos)
    listas_de_ingredientes.append(ingredientes_receta)
    recetas.append(receta)

# Ejecutar el programa
if __name__ == "__main__":
    principal()
