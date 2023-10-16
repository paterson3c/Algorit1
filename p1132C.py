import numpy as np
from typing import Tuple
import p1132A as heap


def min_heap_sort(h: np.ndarray) -> np.ndarray:
    # Create a min heap in-place on h
    heap.create_min_heap(h)
    
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
        heap.min_heapify(h, 0)
    
    return np.array(sorted_array)