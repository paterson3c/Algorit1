import timeit
import random


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
            

l_timings_it = []
l_timings_rec = []
for i, size in enumerate(range(5, 15)):
    t = list(range(2**i * size))

    key = random.randint(0, len(t))
    print(key, bb (t, 0, len(t) - 1, key), rec_bb (t, 0, len(t) - 1, key), '\n')

    timings_it = timeit.timeit(lambda: bb (t, 0, len(t) - 1, key), number=10)
    timings_rec = timeit.timeit(lambda: rec_bb (t, 0, len(t) - 1, key), number=10)

    l_timings_it.append([len(t), timings_it])
    l_timings_rec.append([len(t), timings_rec])

print('tiempos iterativa: ', l_timings_it, '\n')
print('tiempos recursiva: ', l_timings_rec)
    