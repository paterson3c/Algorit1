import numpy as np
import p1132A as heap
from typing import Tuple

def pq_ini() -> np.ndarray:
    return np.array([], dtype=int)

def pq_insert(h: np.ndarray, k: int) -> np.ndarray:
    return heap.insert_min_heap(h, k)

def pq_remove(h: np.ndarray) -> Tuple[int, np.ndarray]:
    #el primer elemento es siempre el de prioridad menor
    min_element = h[0]
    #lo intercambiamos con el último elemento
    h[0] = h[len(h) - 1]
    #eliminamos el último elemento
    h = h[:-1]
    #reordenamos el array
    heap.min_heapify(h, 0)
    
    return (min_element, h)