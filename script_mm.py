import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

def time_function_call(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time

#------------------ TAMAÑOS DEL ARRAY ------------------
sizes = list(range(10, 151, 10))  # Matrix sizes from 10x10 to 150x150, incrementing by 10
custom_times = []
numpy_times = []

for n in sizes:
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    
    custom_times.append(time_function_call(matrix_multiplication, A, B))
    numpy_times.append(time_function_call(np.dot, A, B))

# Now, let's fit these times to a theoretical function f(t) = a*t^3 + b
def f(t, a, b):
    return a * t**3 + b

params_custom, _ = curve_fit(f, sizes, custom_times)
params_numpy, _ = curve_fit(f, sizes, numpy_times)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, custom_times, 'o-', label='Custom Multiplication')
plt.plot(sizes, [f(t, *params_custom) for t in sizes], '--', label='Fit for Custom')
plt.plot(sizes, numpy_times, 's-', label='Numpy dot')
plt.plot(sizes, [f(t, *params_numpy) for t in sizes], '--', label='Fit for Numpy')
plt.xlabel('Matrix Size (n x n)')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.title('Execution Times vs Matrix Size')
plt.grid(True)
plt.show()