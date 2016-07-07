arr=map(int,raw_input().split())
sorted_array=[]
l=len(arr)
for i in range(len(arr)):
    j=l-i
    m=max(arr[:j])
    mpos=arr.index(m)
    temp=arr[j-1]
    arr[j-1]=m
    arr[mpos]=temp
print arr
