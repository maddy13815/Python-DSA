def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        didswap = 0
        for j in range(0, i, 1):
            if arr[j] > arr[j+1]:
                #swap the values
                print('line')
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                didswap = 1
    
        if didswap == 0:
            break

arr = [1, 2, 3, 4, 5]
bubbleSort(arr)
print(arr)