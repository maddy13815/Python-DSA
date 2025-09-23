def InsertionSort(arr):
    for i in range(0,len(arr),1):
        j = i
        while(j>0 and arr[j-1] > arr[j]):
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1                   

arr = [14, 9, 15, 12, 6, 8, 13]
InsertionSort(arr)
print(arr)