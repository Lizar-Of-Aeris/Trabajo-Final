# ==========================================
# main.py
# Integrante: Abigail Morales Ochoa
# ==========================================

from menu import menu
from registro import registrar_compra

def main():
    opcion = menu()

    if opcion == 1:
        registrar_compra()


if __name__ == "__main__":
    main()