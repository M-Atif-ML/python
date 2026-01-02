def quicksort(arr,start,end):
    if start < end:
        partition_point = partition(arr,start,end)
        quicksort(arr,start,partition_point-1)
        quicksort(arr,partition_point+1,end)

def partition(arr,start,end):
    pivot,i,j = arr[end],start,end-1

    while i<j:
        while i < end and arr[i] <= pivot:
            i+=1
        while j > start and arr[j]>= pivot:
            j-=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]

    if arr[i] > pivot:
        arr[i],arr[end] = arr[end],arr[i]
    return i

l = [13,-1,31,34,12,35]
quicksort(l,0,len(l)-1)
print(l)