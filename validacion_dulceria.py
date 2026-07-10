# ==========================================================
# Trabajo Final Fundamentos de Programación I
# registro.py
# Integrante: Almendra Ximena Freyre Arriola
# ==========================================================


from datetime import date

def registrar_compra():
    fecha_compra = date.today()

    fecha_funcion = input("Ingrese la fecha de la función (AAAA-MM-DD): ")

carrito = []

cantidad = int(input("¿Cuántos productos agregará?: "))

for i in range(cantidad):

    print(f"\nProducto {i+1}")



