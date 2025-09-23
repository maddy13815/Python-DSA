def selectionSort(arr):
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        #Found the min now swap the number 
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp

arr = [10, 2, 8, 92, 63]
selectionSort(arr)


print(arr)
