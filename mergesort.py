def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    #till elements on left or right
    while (left <= mid) and (right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    #Till now atleast one has been exhausted
    #if elements are present in left then add all elements
    while left <= mid:
        temp.append(arr[left])
        left += 1
    #If elements are present in right then add all elements
    while right <= high:
        temp.append(arr[right])
        right += 1

    #now we have the correct data in temp. Need to move it to original array
    for i in range(low, high+1):
        arr[i] = temp[i-low]


def msort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    msort(arr, low, mid)
    msort(arr, mid+1, high)
    merge(arr, low, mid, high)

def mergesort(arr):
    length = len(arr)
    low = 0
    high = length - 1

    msort(arr, low, high)
    return arr

arr = [4,1,9,10,7,2,3]
print(mergesort(arr))