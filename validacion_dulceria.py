# ==========================================================
# Trabajo Final Fundamentos de Programación I
# registro.py
# Integrante: Almendra Ximena Freyre Arriola
# ==========================================================


from datetime import date

def registrar_compra():

    #Solicita fecha
    fecha_compra = date.today()

    while True:
        fecha_funcion_texto = input("Ingrese la fecha de la función (AAAA-MM-DD): ")
        try:
            fecha_funcion = date.fromisoformat(fecha_funcion_texto)
            break
        except ValueError:
            print("Formato invalido. Use AAAA-MM-DD con guiones. Ej: 2026-07-10")

    #Solicita cantidad de productos
    carrito = [ ]

    while True:
        cantidad_texto = input("¿Cuántos productos agregará?: ")
        if cantidad_texto.isdigit() and int(cantidad_texto) > 0:
            cantidad = int(cantidad_texto)
            break
        else:
            print("Ingrese un número entero mayor a 0, sin letras ni símbolos.")


    #Desarrolla ciclo for
    for i in range(cantidad):

        print(f"\nProducto {i+1}")

        nombre = input("Nombre: ")
        tipo = input("Tipo (entrada/dulceria): ").lower()
        precio = float(input("Precio: "))

    #Agrega al carrito
        carrito.append({
            "nombre": nombre,
            "tipo": tipo,
            "precio": precio
        })


return fecha_compra, fecha_función, carrito


    

