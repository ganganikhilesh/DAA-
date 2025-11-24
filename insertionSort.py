import random
import time
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
sizes = [10, 100, 500, 1000,2000, 5000]  
for i in sizes:
    arr = [random.randint(1, 10000) for j in range(i)]
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    run_time = end - start
    print(f"Array Size = {i:6d}:Execution Time = {run_time:.6f}sec")