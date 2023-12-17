import numpy as np
from typing import Tuple

### ------------------- 1A ------------------- ###
def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray) -> np.ndarray:
    """
    Realiza la multiplicación de dos matrices m_1 y m_2.

    Args:
        m_1 (np.ndarray): Primera matriz.
        m_2 (np.ndarray): Segunda matriz.

    Returns:
        np.ndarray: Matriz resultante de la multiplicación de m_1 y m_2.

    Detalles:
        - Verifica que el número de columnas en m_1 sea igual al número de filas en m_2.
        - Realiza la multiplicación matricial de forma iterativa.
    """
    t1 = m_1.shape
    t2 = m_2.shape
    m_3 = np.zeros([t1[0], t2[1]])  # Inicializa la matriz resultante

    if t1[1] != t2[0]:  # Verifica si la multiplicación es posible
        return
    
    for i in range(t1[0]):  # Itera sobre filas de m_1
        for k in range(t2[1]):  # Itera sobre columnas de m_2
            for j in range(t1[1]):  # Itera sobre columnas de m_1 y filas de m_2
                m_3[i][k] += m_1[i][j] * m_2[j][k]
            
    return m_3

### ------------------- 1B ------------------- ###
def rec_bb(t: list, f: int, l: int, key: int) -> int:
    """
    Implementa la búsqueda binaria de manera recursiva.

    Args:
        t (list): Lista donde buscar.
        f (int): Índice inicial.
        l (int): Índice final.
        key (int): Elemento a buscar.

    Returns:
        int: Índice del elemento encontrado o None si no se encuentra.

    Detalles:
        - Divide el rango de búsqueda en dos y realiza la búsqueda en la mitad correspondiente.
    """
    mid = (f + l) // 2  # Encuentra el índice medio

    if f > l:  # Verifica si se ha terminado la búsqueda
        return

    if t[mid] == key:  # Elemento encontrado
        return mid
    elif t[mid] > key:  # Busca en la mitad izquierda
        return rec_bb(t, f, mid - 1, key)
    else:  # Busca en la mitad derecha
        return rec_bb(t, mid + 1, l, key)
    
def bb(t: list, f: int, l: int, key: int) -> int:
    """
    Implementa la búsqueda binaria de manera iterativa.

    Args:
        t (list): Lista donde buscar.
        f (int): Índice inicial.
        l (int): Índice final.
        key (int): Elemento a buscar.

    Returns:
        int: Índice del elemento encontrado o None si no se encuentra.

    Detalles:
        - Divide el rango de búsqueda en dos y ajusta los índices según sea necesario.
    """
    while f <= l:  # Mientras haya elementos para buscar
        mid = (f + l) // 2  # Encuentra el índice medio
        if t[mid] < key:  # Ajusta el índice inicial si el elemento es mayor
            f = mid + 1
        elif t[mid] > key:  # Ajusta el índice final si el elemento es menor
            l = mid - 1
        else:  # Elemento encontrado
            return mid
    
    return  # Elemento no encontrado

### ------------------- 2A ------------------- ###
def min_heapify(h: np.ndarray, i: int):
    """
    Transforma un subárbol en un min-heap.

    Args:
        h (np.ndarray): Arreglo que representa un heap.
        i (int): Índice del nodo raíz del subárbol.

    Detalles:
        - Compara el nodo con sus hijos y realiza intercambios para mantener la propiedad de min-heap.
        - Se llama recursivamente para asegurar que los subárboles también sean min-heaps.
    """
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho
    n = len(h)  # Tamaño del heap
    smallest = i  # Inicialmente, asume que el nodo actual es el más pequeño

    # Compara con el hijo izquierdo
    if left < n and h[left] < h[smallest]:
        smallest = left
    # Compara con el hijo derecho
    if right < n and h[right] < h[smallest]:
        smallest = right
    # Intercambia y llama a min_heapify si el nodo actual no es el más pequeño
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        min_heapify(h, smallest)
    return

def create_min_heap(h: np.ndarray):
    """
    Crea un min-heap a partir de un arreglo dado.

    Args:
        h (np.ndarray): Arreglo a convertir en min-heap.

    Detalles:
        - Llama a min_heapify para cada nodo que tiene al menos un hijo.
    """
    for i in range(len(h) // 2, -1, -1):  # Comienza desde el último nodo con hijos
        min_heapify(h, i)

def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray:
    """
    Inserta un elemento en un min-heap.

    Args:
        h (np.ndarray): Min-heap.
        k (int): Elemento a insertar.

    Returns:
        np.ndarray: Min-heap con el elemento insertado.

    Detalles:
        - Añade el elemento al final y lo reubica para mantener la propiedad de min-heap.
    """
    h = np.append(h, k)  # Añade el elemento al final
    idx = len(h) - 1  # Índice del elemento añadido
    # Reubica el elemento hacia arriba en el heap si es necesario
    while idx > 0:
        parent = (idx - 1) // 2  # Índice del nodo padre
        if h[idx] < h[parent]:  # Intercambia si el hijo es menor que el padre
            h[idx], h[parent] = h[parent], h[idx]
            idx = parent  # Actualiza el índice para seguir comparando hacia arriba
        else:
            break
    return h

### ------------------- 2B ------------------- ###
def pq_ini() -> np.ndarray:
    """
    Inicializa una cola de prioridad (priority queue) vacía.

    Returns:
        np.ndarray: Cola de prioridad vacía.
    """
    return np.array([])

def pq_insert(h: np.ndarray, k: int) -> np.ndarray:
    """
    Inserta un elemento en la cola de prioridad.

    Args:
        h (np.ndarray): Cola de prioridad.
        k (int): Elemento a insertar.

    Returns:
        np.ndarray: Cola de prioridad con el elemento insertado.

    Detalles:
        - Utiliza insert_min_heap para mantener la propiedad de min-heap.
    """
    return insert_min_heap(h, k)

def pq_remove(h: np.ndarray) -> Tuple[int, np.ndarray]:
    """
    Remueve el elemento de menor prioridad (el menor elemento) de la cola de prioridad.

    Args:
        h (np.ndarray): Cola de prioridad.

    Returns:
        Tuple[int, np.ndarray]: El elemento removido y la cola de prioridad actualizada.

    Detalles:
        - Intercambia el primer elemento (el menor) con el último y lo elimina.
        - Llama a min_heapify para restaurar la propiedad de min-heap.
    """
    min_element = h[0]  # El primer elemento es siempre el menor en un min-heap
    h[0] = h[-1]  # Intercambia con el último elemento
    h = h[:-1]  # Elimina el último elemento (ahora el más pequeño)
    min_heapify(h, 0)  # Restaura la propiedad de min-heap
    return (min_element, h)

### ------------------- 2C ------------------- ###
def min_heap_sort(h: np.ndarray) -> np.ndarray:
    """
    Ordena un arreglo utilizando el enfoque de min-heap.

    Args:
        h (np.ndarray): Arreglo a ordenar.

    Returns:
        np.ndarray: Arreglo ordenado.

    Detalles:
        - Convierte el arreglo en un min-heap y luego extrae el elemento más pequeño sucesivamente.
    """
    create_min_heap(h)  # Convierte el arreglo en un min-heap
    sorted_array = []  # Arreglo para almacenar los elementos ordenados
    n = len(h)  # Número de elementos
    for _ in range(n):
        sorted_array.append(h[0])  # Añade el elemento más pequeño al arreglo ordenado
        h[0] = h[-1]  # Mueve el último elemento a la raíz
        h = h[:-1]  # Elimina el último elemento
        min_heapify(h, 0)  # Reconstruye el min-heap
    return np.array(sorted_array)  # Devuelve el arreglo ordenado
