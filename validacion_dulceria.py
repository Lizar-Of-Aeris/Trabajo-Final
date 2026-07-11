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
            print("Formato invalido. Use AAAA-MM-DD con guiones. Ej: 2026-07-10")


        


    

