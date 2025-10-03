# def brute(arr):
#     #loop over array and store it in set
#     arrset = set()
#     write_index = 0
#     for i in range(len(arr)):
#         if arr[i] not in arrset:
#             arrset.add(arr[i])
#             arr[write_index] = arr[i]
#             write_index += 1
    
#     return write_index

def optimal(arr):
    i = 0
    arrlen = len(arr)
    for j in range(1, arrlen, 1):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
        
    return i

arr = [1,1,2,2,2,3,3]
# print(brute(arr))
print(optimal(arr))
print(arr)