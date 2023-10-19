import numpy as np
import matplotlib.pyplot as plt
import time

def min_heapify(h: np.ndarray, i: int):
    left = 2 * i + 1
    right = 2 * i + 2
    n = len(h)
    smallest = i
    
    if left < n and h[left] < h[smallest]:
        smallest = left
    if right < n and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        min_heapify(h, smallest)
    return

def create_min_heap(h: np.ndarray):
    for i in range(len(h) // 2, -1, -1):
        min_heapify(h, i)

def min_heap_sort(h: np.ndarray) -> np.ndarray:
    # Create a min heap in-place on h
    create_min_heap(h)
    
    sorted_array = []
    n = len(h)
    for _ in range(n):
        # Extract the smallest element (root of the min heap)
        sorted_array.append(h[0])
        
        # Copy the last element to the root
        h[0] = h[-1]
        
        # Reduce the size of the heap
        h = h[:-1]
        
        # Rebuild the min heap
        min_heapify(h, 0)
    
    return np.array(sorted_array)

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

def plot_times():
    # ------------------ TAMAÑOS DEL ARRAY ------------------
    sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    create_min_heap_times = []
    min_heap_sort_times = []

    for size in sizes:
        # Generar datos aleatorios
        data = np.random.randint(0, 100000, size)

        # Medir tiempo para create_min_heap
        heap_time = measure_time(create_min_heap, data.copy())
        create_min_heap_times.append(heap_time)

        # Medir tiempo para min_heap_sort
        sort_time = measure_time(min_heap_sort, data.copy())
        min_heap_sort_times.append(sort_time)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, create_min_heap_times, 'o-', label='create_min_heap')
    plt.plot(sizes, min_heap_sort_times, 's-', label='min_heap_sort')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo de ejecución vs. Tamaño de entrada')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejecutar la función para graficar
plot_times()