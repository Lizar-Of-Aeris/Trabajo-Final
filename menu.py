# ==========================================
# menu.py
# Integrante: Abigail Morales Ochoa
# ==========================================

PELICULAS = {
    1: "Lilo & Stitch",
    2: "Jurassic World",
    3: "Superman",
    4: "Minecraft"
}


def mostrar_cartelera():
    print("\n========== CARTELERA ==========")

    for codigo, pelicula in PELICULAS.items():
        print(codigo, "-", pelicula)


def menu():
    while True:
        print("\n====================================")
        print("      CINE STAR - AUTOSERVICIO")
        print("====================================")
        print("1. Realizar compra")
        print("2. Ver cartelera")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            return 1

        elif opcion == "2":
            mostrar_cartelera()
            input("\nPresione ENTER para volver al menú...")

        elif opcion == "3":
            print("\nGracias por utilizar nuestro sistema.")
            return 0

        else:
            print("\nOpción inválida. Intente nuevamente.")