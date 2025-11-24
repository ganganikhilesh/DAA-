import time
import random
def countsort(arr):
    max_el=max(arr)
    count_arr=[0]*(max_el+1)
    for i in arr:
        count_arr[i]+=1
    for i in range(max_el):
        count_arr[i+1]+=count_arr[i]
    result=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        result[count_arr[arr[i]]-1]=arr[i]
        count_arr[arr[i]]-=1
    return result
sizes=[10,100,500,1000,2000]
for i in sizes:
    arr=[random.randint(1,10000) for j in range(i)]
    start = time.time()
    countsort(arr)
    end = time.time()
    run_time = end - start
    print(f"Array_size={i:6d}:run_time={run_time:.6f}sec")