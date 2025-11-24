import random
import time
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertionSort(self, value):
        new_node = Node(value)
        if self.head==None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node


def bucket_sort(arr):
    if len(arr) == 0:
        return []

    num = len(arr)
    buckets = [LinkedList() for i in range(num)]

    for value in arr:
        index = int(value * num)
        buckets[index].insertionSort(value)

    sorted_array = []
    for bucket in buckets:
            current = bucket.head
            while current:
                sorted_array.append(current.value)
                current = current.next
    return sorted_array

sizes=[10,100,500,1000,2000]
for i in sizes:
    # since by using random.uniform we get equal to 1 if we include it that's why i include 0.999
    arr=[round(random.uniform(0,0.999),3) for j in range(i)]
    start = time.time()
    bucket_sort(arr)
    end = time.time()
    run_time = end - start
    print(f"Array_size={i:6d}:run_time={run_time:.6f}sec")
