import random
import time
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
sizes = [10, 100, 500, 1000, 2000]
for i in sizes:
    arr=[random.randint(1,10000) for j in range(i)]
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    run_time = end - start
    print(f"Array_size={i:6d}:run_time={run_time:.6f}sec")