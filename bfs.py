def bfs(arr, s):
    n=len(arr)
    visited=[0] * n
    queue=[s]
    visited[s]=1

    print("BFS Traversal:",end=" ")

    while queue:
        node=queue.pop(0)
        print(node,end=" ")

        for i in range(n):
            if arr[node][i] == 1 and visited[i]==0:
                queue.append(i)
                visited[i] = 1
arr = [
    [0,1,1,0,0,1],
    [1,0,0,1,0,0],
    [1,0,0,1,1,0],
    [0,1,1,0,1,1],
    [0,0,1,1,0,0],
    [1,0,0,1,0,0]
]


bfs(arr,3)