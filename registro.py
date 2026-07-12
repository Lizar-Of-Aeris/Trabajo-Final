# ==========================================================
# Trabajo Final Fundamentos de Programación I
# registro.py
# Integrante: Almendra Ximena Freyre Arriola
# ==========================================================


from datetime import date
from menu import PELICULAS, mostrar_cartelera
from cantidades import gestionar_cantidades_y_carrito
from ticket import generar_ticket
from validacion import validar_compra

HORARIOS = {1: "2:00 PM", 2: "5:00 PM", 3: "8:00 PM"}

TIPOS_ENTRADA = {
    1: ("Entrada adulto", 20.00),
    2: ("Entrada niño", 15.00),
    3: ("Entrada adulto mayor", 12.00)
}

def registrar_compra():

    fecha_compra = date.today()

    #Selección de película
    mostrar_cartelera()

    while True:
        opcion_pelicula = input("\nSeleccione una película: ")

        if opcion_pelicula.isdigit() and int(opcion_pelicula) in PELICULAS:
            pelicula = PELICULAS[int(opcion_pelicula)]
            break

        else:
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

        else:
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

        else:
            print("Opción de entrada inválida.")


    fecha_compra, fecha_funcion, pelicula, horario, carrito = gestionar_cantidades_y_carrito(fecha_compra, fecha_funcion, pelicula, horario, entrada_seleccionada)
    advertencias = validar_compra(fecha_compra, fecha_funcion, carrito)
    
    generar_ticket(pelicula, fecha_funcion, horario, carrito, advertencias)

