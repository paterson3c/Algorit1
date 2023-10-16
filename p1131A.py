import numpy as np
import timeit


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

l_timings_alg = []
l_timings_dot = []
for i in range(10, 11):
    dim = 10+i**2
    m = np.random.uniform(0., 1., [dim, dim])

    timings_dot = timeit.timeit(lambda: np.dot(m, m), number=10)
    timings_alg = timeit.timeit(lambda: matrix_multiplication(m, m), number=10)

    l_timings_alg.append([dim, timings_alg])
    l_timings_dot.append([dim, timings_dot])

print('tiempos algoritmo: ', l_timings_alg)
print('tiempos dot: ', l_timings_dot)