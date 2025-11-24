import time
start=time.time()
def binarysearch(arr,left,right,s):
    if(left>right):
        return -1
    m=(left+right)//2
    if(arr[m]==s):
        return m
    elif(arr[m]>=s):
        return binarysearch(arr,left,m-1,s)
    else:
        return binarysearch(arr,m+1,right,s)
arr=[1,2,3,4,5,6,7,8,9]
s=int(input("enter the number you want search:"))
print(binarysearch(arr,0,len(arr)-1,s))
end=time.time()
time=end-start