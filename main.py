import time
import sys
import Clase_Pokemon


# Delay al escribir
def delay_print(s):
    # Imprimir una letra a la vez
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

