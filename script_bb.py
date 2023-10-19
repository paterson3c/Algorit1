import numpy as np
import matplotlib.pyplot as plt
import time

# Búsqueda binaria recursiva
def rec_bb (t: list, f: int, l: int, key: int)-> int:
    mid = (f + l) // 2

    if(f > l):
        return

    if (t[mid] == key):
        return mid
    elif (t[mid] > key):
        return (rec_bb (t, f, (mid - 1), key))
    elif (t[mid] < key):
        return (rec_bb (t, (mid + 1), l, key))

# Búsqueda binaria iterativa
def bb (t: list, f: int, l: int, key: int)-> int:
    
    mid = 0

    while f <= l:
        mid = (f + l) // 2

        if (t[mid] < key):
            f = mid + 1
        elif (t[mid] > key):
            l = mid - 1
        else:
            return mid
    
    return

# Medir tiempos y graficar
# ------------------ TAMAÑOS DEL ARRAY ------------------
sizes = [2**i for i in range(10, 21)] 
rec_times = []
it_times = []

for size in sizes:
    t = list(range(size))
    key = -1  # Una clave que no está en la lista

    # Medir tiempo para búsqueda recursiva
    start_time = time.time()
    rec_bb(t, 0, len(t) - 1, key)
    end_time = time.time()
    rec_times.append(end_time - start_time)

    # Medir tiempo para búsqueda iterativa
    start_time = time.time()
    bb(t, 0, len(t) - 1, key)
    end_time = time.time()
    it_times.append(end_time - start_time)

# Graficar
plt.plot(sizes, rec_times, label='Recursiva', marker='o')
plt.plot(sizes, it_times, label='Iterativa', marker='x')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (s)')
plt.legend()
plt.title('Comparación de tiempos de ejecución: Búsqueda Binaria')
plt.show()