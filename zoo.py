from animal import Animal, Mamifero, Ave


animales = []

def mostrar_menu():
    print("\n--- MENÚ DEL ZOOLÓGICO ---")
    print("1. Agregar animal")
    print("2. Alimentar animales")
    print("3. Mostrar todos los animales")
    print("4. Salir")

def agregar_animal():
    print("\nTipos de animales:")
    print("1. Animal básico")
    print("2. Mamífero")
    print("3. Ave")
    
    tipo = input("Elige el tipo (1-3): ")
    nombre = input("Nombre del animal: ")
    especie = input("Especie: ")
    
    if tipo == "1":
        animal = Animal(nombre, especie)
    elif tipo == "2":
        pelaje = input("Tipo de pelaje: ")
        animal = Mamifero(nombre, especie, pelaje)
    elif tipo == "3":
        envergadura = input("Envergadura (cm): ")
        animal = Ave(nombre, especie, envergadura)
    else:
        print("Opción no válida, se creará animal básico")
        animal = Animal(nombre, especie)
    
    animales.append(animal)
    print(f"{nombre} ha sido agregado al zoológico")

def alimentar_animales():
    if not animales:
        print("No hay animales para alimentar")
        return
    
    print("\nAlimentando animales:")
    for animal in animales:
        animal.alimentar()

def mostrar_animales():
    if not animales:
        print("No hay animales en el zoológico")
        return
    
    print("\nAnimales en el zoológico:")
    for i, animal in enumerate(animales, 1):
        print(f"{i}. {animal.mostrar_info()}")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        agregar_animal()
    elif opcion == "2":
        alimentar_animales()
    elif opcion == "3":
        mostrar_animales()
    elif opcion == "4":
        print("¡Gracias por visitar el zoológico!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

