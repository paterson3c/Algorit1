import numpy as np

def min_heapify(h: np.ndarray, i: int, n: int):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    
    if left < n and h[left] < h[smallest]:
        smallest = left
    if right < n and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        min_heapify(h, smallest, n)

def create_min_heap(h: np.ndarray):
    for i in range(len(h) // 2, -1, -1):
        min_heapify(h, i, len(h))

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


if __name__ == '__main__':
    h = np.array([3, 2, 1, 5, 4])
    create_min_heap(h)
    print(h)

    h = insert_min_heap(h, 0)
    print(h)

    