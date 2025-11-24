def dfs(arr,s):
    n=len(arr)
    visited=[0]*n
    stack=[s]

    print("DFS Traversal:",end=" ")

    while stack:
        element=stack.pop()
        if visited[element]==0:
            print(element, end=" ")
            visited[element]=1
            for i in range(n):
                if arr[element][i]==1 and visited[i]==0:
                    stack.append(i)

arr = [
    [0,1,1,0,0,1],
    [1,0,0,1,0,0],
    [1,0,0,1,1,0],
    [0,1,1,0,1,1],
    [0,0,1,1,0,0],
    [1,0,0,1,0,0]
]
dfs(arr,0)