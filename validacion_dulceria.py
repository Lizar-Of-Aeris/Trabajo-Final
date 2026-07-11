# ==========================================================
# Trabajo Final Fundamentos de Programación I
# registro.py
# Integrante: Almendra Ximena Freyre Arriola
# ==========================================================


from datetime import date
from menu import PELICULAS, mostrar_cartelera

HORARIOS = {1: "2:00 PM", 2: "5:00 PM", 3: "8:00 PM"}

TIPOS_ENTRADA = {
    1: ("Entrada adulto", 20.00),
    2: ("Entrada niño", 15.00),
    3: ("Entrada adulto mayor", 12.00)
}

PRODUCTOS_DULCERIA = {
    1: ("Canchita grande", 18.00),
    2: ("Combo familiar", 35.00),
    3: ("Gaseosa", 10.00),
    4: ("Hot dog", 12.00),
    5: ("Nachos", 16.00)
}

def registrar_compra():

    fecha_compra = date.today()
    carrito = [ ]

    #Selección de película
    mostrar_cartelera()

    while True:
        opcion_pelicula = input("\nSeleccione una película: ")

        if opcion_pelicula.isdigit() and int(opcion_pelicula) in PELICULAS:
            pelicula = PELICULAS (int(opcion_pelicula))
            break

        print("Opción de película inválida.")

    
    #Fecha de la función
    while True:
        fecha_funcion_texto = input("\nIngrese la fecha de la función (AAAA-MM-DD): ")
        
        try:
            fecha_funcion = date.fromisoformat(fecha_funcion_texto)
            break

        except ValueError:
            print("Formato inválido. Use AAAA-MM-DD con guiones. Ej: 2026-07-10")

    #Selección de horario
    print("\n=================== HORARIOS ===================")

    for codigo, horario_disponible in HORARIOS.items():
        print(codigo, "-", horario_disponible)

    while True:
        opcion_horario = input("\nSeleccione un horario: ")
        if opcion_horario.isdigit() and int(opcion_horario) in HORARIOS:
            horario = HORARIOS[int(opcion_horario)]
            break
        print("Opción de horario inválida.")
        
    #Selección del tipo de entrada
    print("\n=================== ENTRADAS ===================")

    for codigo, entrada in TIPOS_ENTRADA.items():
        print(codigo, "-", entrada[0], "-S/.", entrada[1])

    while True:
        opcion_entrada = input("\nSeleccione el tipo de entrada: ")

        if opcion_entrada.isdigit() and int(opcion_entrada) in TIPOS_ENTRADA:
            entrada_seleccionada = TIPOS_ENTRADA[int(opcion_entrada)]
            break
        print("Opción de entrada inválida.")

    #Cantidad de entradas
    while True
        cantidad_texto = input("Ingrese la cantidad de entradas: ")
        if cantidad_texto.isdigit() and int(cantidad_texto) > 0:
            cantidad_entradas = int(cantidad_texto)
            break
        print("Ingrese una cantidad válida.")

    for i in range(cantidad_entradas):
        carrito.append({
            "nombre": entrada_seleccionada[0],
            "tipo": "entrada",
            "precio": entrada_seleccionada[1]
        })





return fecha_compra, fecha_funcion, pelicula, horario, carrito
    

