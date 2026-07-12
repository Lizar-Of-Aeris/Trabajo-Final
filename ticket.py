# ==========================================
# ticket.py
# Integrante: Diego Orlando Leandro Pinto
# ==========================================

def generar_ticket(
        pelicula,
        fecha_funcion,
        horario,
        carrito,
        advertencias):

    # Mostrar advertencia si la función es para otra fecha
    if len(advertencias) > 0:

        print("\n====================================")
        print("             ADVERTENCIA")
        print("====================================")

        print(
            "Los siguientes productos de dulcería "
            "solo pueden recogerse el mismo día:"
        )

        for producto in advertencias:
            print("-", producto["nombre"])

        while True:
            respuesta = input(
                "\n¿Desea eliminarlos del carrito? (S/N): "
            ).upper()

            if respuesta == "S":
                nuevo_carrito = []

                for producto in carrito:

                    if producto not in advertencias:
                        nuevo_carrito.append(producto)

                carrito = nuevo_carrito
                print("\nLos productos fueron eliminados.")
                break

            elif respuesta == "N":
                print(
                    "\nLos productos se mantendrán "
                    "en la compra."
                )
                break

            else:
                print("Ingrese solamente S o N.")

    # Generación del ticket
    total = 0

    print("\n====================================")
    print("          TICKET DE COMPRA")
    print("====================================")
    print("Película:", pelicula)
    print("Fecha de función:", fecha_funcion)
    print("Horario:", horario)

    print("\nDetalle de productos:")

    for producto in carrito:
        print(
            producto["nombre"],
            "- S/.",
            format(producto["precio"], ".2f")
        )

        total += producto["precio"]

    print("------------------------------------")
    print("TOTAL: S/.", format(total, ".2f"))
    print("\n¡Gracias por su compra!")