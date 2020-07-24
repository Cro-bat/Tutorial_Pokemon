# Crear la clase
import time
import numpy as np


class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, vida="=========="):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ATAQUE']
        self.defensa = EVs['DEFENSA']
        self.barras = 20

    def pelea(self, Pokemon2):
        print("----BATALLA POKEMON----")
        print(f"\n{self.name}")
        print("TIPO/", self.tipos)
        print("ATAQUE/", self.ataque)
        print("DEFENSA/", self.defensa)
        print("NIVEL/", 3 * (1 + np.mean([self.ataque, self.defensa])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TIPO/", Pokemon2.tipos)
        print("ATAQUE/", Pokemon2.ataque)
        print("DEFENSA/", Pokemon2.defensa)
        print("NIVEL/", 3 * (1 + np.mean([Pokemon2.ataque, Pokemon2.defensa])))

        time.sleep(2)

        # ventajas de tipos
        version = ['Fuego', 'Agua', 'Planta']
        for i, k in enumerate(version):
            if self.types == k:
                # Mismo tipo
                if Pokemon2.tipos == k:
                    string_1_ataque = "No es muy efectivo..."
                    string_2_ataque = "No es muy efectivo..."

                # Pokemon 2 es fuerte
                if Pokemon2.tipos == version[(i + 1) % 3]:
                    string_1_ataque = "No es muy efectivo..."
                    string_2_ataque = "No es muy efectivo..."
