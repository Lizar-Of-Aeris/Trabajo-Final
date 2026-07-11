# ==========================================================
# Trabajo Final Fundamentos de Programación I
# registro.py
# Integrante: Almendra Ximena Freyre Arriola
# ==========================================================


from datetime import date

def registrar_compra():

    #Solicita fecha
    fecha_compra = date.today()

    fecha_función = input("Ingrese la fecha de la función (AAAA-MM-DD): ")

    #Solicita cantidad de productos
    carrito = [ ]

    cantidad = int(input("¿Cuántos productos agregará?: "))

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


    

