import numpy as np
from typing import Tuple


### ------------------- 1A ------------------- ###
def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:

    t1 = m_1.shape
    t2 = m_2.shape

    m_3 = np.zeros([t1[0], t2[1]])

    if t1[1] != t2[0]:
        return
    
    for i in range(t1[0]):
        for k in range(t2[1]):
            for j in range(t1[1]):
                m_3[i][k] += m_1[i][j] * m_2[j][k]
            
    return m_3


### ------------------- 1B ------------------- ###
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


### ------------------- 2A ------------------- ###
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

def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray:
    h = np.append(h, k)
    idx = len(h) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if h[idx] < h[parent]:
            h[idx], h[parent] = h[parent], h[idx]
            idx = parent
        else:
            break
    return h



### ------------------- 2B ------------------- ###
def pq_ini() -> np.ndarray:
    return np.array([])

def pq_insert(h: np.ndarray, k: int) -> np.ndarray:
    return insert_min_heap(h, k)

def pq_remove(h: np.ndarray) -> Tuple[int, np.ndarray]:
    #el primer elemento es siempre el de prioridad menor
    min_element = h[0]
    #lo intercambiamos con el último elemento
    h[0] = h[-1]
    #eliminamos el último elemento
    h = h[:-1]
    #reordenamos el array
    min_heapify(h, 0)
    
    return (min_element, h)

### ------------------- 2C ------------------- ###
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