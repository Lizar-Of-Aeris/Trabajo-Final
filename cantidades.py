# ==========================================
# cantidades.py
# Integrante :Frank Nicolas Ferrer
# ==========================================

PRODUCTOS_DULCERIA = {
    1: ("Canchita grande", 18.00),
    2: ("Combo familiar", 35.00),
    3: ("Gaseosa", 10.00),
    4: ("Hot dog", 12.00),
    5: ("Nachos", 16.00)
}

def gestionar_cantidades_y_carrito(fecha_compra, fecha_funcion, pelicula, horario, entrada_seleccionada):
    # Inicializa el carrito en esta etapa
    carrito = []

    # Cantidad de entradas
    while True:
        cantidad_texto = input("\nIngrese la cantidad de entradas: ")
        if cantidad_texto.isdigit() and int(cantidad_texto) > 0:
            cantidad_entradas = int(cantidad_texto)
            break
        print("Ingrese una cantidad válida.")

    # Llenado de entradas al carrito
    for i in range(cantidad_entradas):
        carrito.append({
            "nombre": entrada_seleccionada[0],
            "tipo": "entrada",
            "precio": entrada_seleccionada[1]
        })

    # Productos de dulcería
    respuesta = input("\n¿Desea agregar productos de dulcería? (S/N): ").upper()

    while respuesta == "S":
        print("\n========== DULCERÍA ==========")
        for codigo, producto in PRODUCTOS_DULCERIA.items():
            print(codigo, "-", producto[0], "- S/.", producto[1])
        print("6 - Finalizar selección")

        opcion_producto = input("\nSeleccione un producto: ")

        if not opcion_producto.isdigit():
            print("Ingrese una opción numérica.")
            continue

        opcion_producto = int(opcion_producto)

        if opcion_producto == 6:
            break
        elif opcion_producto in PRODUCTOS_DULCERIA:
            producto_seleccionado = PRODUCTOS_DULCERIA[opcion_producto]
            carrito.append({
                "nombre": producto_seleccionado[0],
                "tipo": "dulceria",
                "precio": producto_seleccionado[1]
            })
            print(producto_seleccionado[0], "fue agregado al carrito.")
        else:
            print("Producto no válido.")

    # Retorno final hacia el programa principal
    return fecha_compra, fecha_funcion, pelicula, horario, carrito
