# Crear la clase
import time
import numpy as np
import Funciones


class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, vida = "=========="):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ATAQUE']
        self.defensa = EVs['DEFENSA']
        self.vida = vida
        self.barras = 20

    def pelea(self, Pokemon2):
        global string_1_ataque
        print("----BATALLA POKEMON----")
        print(f"\n{self.nombre}")
        print("TIPO/", self.tipos)
        print("ATAQUE/", self.ataque)
        print("DEFENSA/", self.defensa)
        print("NIVEL/", 3 * (1 + np.mean([self.ataque, self.defensa])))
        print("\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("TIPO/", Pokemon2.tipos)
        print("ATAQUE/", Pokemon2.ataque)
        print("DEFENSA/", Pokemon2.defensa)
        print("NIVEL/", 3 * (1 + np.mean([Pokemon2.ataque, Pokemon2.defensa])))

        time.sleep(2)

        # ventajas de tipos
        version = ['Fuego', 'Agua', 'Planta']
        for i, k in enumerate(version):
            if self.tipos == k:
                # Mismo tipo
                if Pokemon2.tipos == k:
                    string_1_ataque = "\nNo es muy efectivo..."
                    string_2_ataque = "\nNo es muy efectivo..."

                # Pokemon 2 es fuerte
                if Pokemon2.tipos == version[(i + 1) % 3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    string_1_ataque = "\nNo es muy efectivo..."
                    string_2_ataque = "\nEs muy eficaz!"

                # Pokemon 2 es debil
                if Pokemon2.tipos == version[(i + 2) % 3]:
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    self.ataque *= 2
                    self.defensa *= 2
                    string_1_ataque = "\nEs muy eficaz!"
                    string_2_ataque = "\nNo es muy efectivo..."

        # Ciclo de pelea
        while (self.barras > 0) and (Pokemon2.barras > 0):
            print(f"{self.nombre}\t\tHP\t{self.vida}")
            print(f"{Pokemon2.nombre}\t\tHP\t {Pokemon2.vida}\n")

            print(f"Adelante {self.nombre}!")

            for i, x in enumerate(self.movimientos):
                print(f"{i + 1}.", x)
            index = int(input("Elige un movimiento: "))
            Funciones.delay_print(string_1_ataque)

            print(f"\n{self.nombre} usó {self.movimientos[index-1]}")

            #Determinar daño
            Pokemon2.barras -= self.ataque
            Pokemon2.vida = ""

            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.vida += "="


            time.sleep(1)
            print(f"\n{self.nombre}\t\tHP\t{Pokemon2.vida}")
            print(f"{Pokemon2.nombre}\t\tHP\t{self.vida}\n")
            time.sleep(.5)

            #Comprobar debilitado
            if Pokemon2.barras <= 0:
                Funciones.delay_print("\n..." + Pokemon2.nombre + ' se ha debilitado.')
                break

            #Turno Pokemon 2

            print(f"Adelante {Pokemon2.nombre}!")

            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i + 1}.", x)
            index = int(input("Elige un movimiento: "))
            Funciones.delay_print(string_2_ataque)

            print(f"\n{Pokemon2.nombre} usó {Pokemon2.movimientos[index - 1]}")

            # Determinar daño
            self.barras -= Pokemon2.ataque
            self.vida = ""

            for j in range(int(self.barras + .1 * self.defensa)):
                self.vida += "="

            time.sleep(1)
            print(f"\n{Pokemon2.nombre}\t\tHP\t{Pokemon2.vida}")
            print(f"{self.nombre}\t\tHP\t{self.vida}\n")
            time.sleep(.5)

            # Comprobar debilitado
            if self.barras <= 0:
                Funciones.delay_print("..." + self.nombre + ' se ha debilitado.')
                break

        dinero = np.random.choice(5000)
        Funciones.delay_print(f"\nTu oponente te ha pagado ${dinero}.")
