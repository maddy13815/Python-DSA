# "def swap(a,b):
#     temp = b
#     b = a
#     a = temp

# def findindexandpivot(arr, low, high):
#     pivot =  arr[low] #get the pivot as the lowest element
#     i = low #make i and j pointer at the two extreme points and compare them 
#     j = high  

#     while(i<j): #till i crosses j or vice versa
#         #check if value at i position is greater than the value at pivot if yes then stop incrementing i otherwise move it to right
#         while(arr[i] <= pivot and i <= high-1):
#             i += 1
#         #check if value at j position is less than value at pivot if yes then stop otherwise move it to left
#         while(arr[j] > pivot and j >= low+1 ):
#             j -= 1

#         #Now we have found the value from i and j now swap both the values
#         if i < j:
#             temp = arr[j]
#             arr[j] = arr[i]
#             arr[i] = temp

#     #Now swap the pivot element with the j th element to fix it at correct position
#     temp2 = arr[j]
#     arr[j] = arr[low]
#     arr[low] = temp2   
#     return j


# def qsort(arr, low, high):
#     if low < high:
#         pindex = findindexandpivot(arr, low, high)
#         qsort(arr, low, pindex - 1 )
#         qsort(arr, pindex+1, high)

# def quicksort(arr):
#     low = 0
#     high = len(arr)-1
#     qsort(arr, low, high)
#     return arr




# arr = [4,1,9,10,7,2,3]
# print(quicksort(arr))

##################################################################
class Solution:
    def fixpivot(self, arr, low, high):
        pivot =  arr[low] #get the pivot as the lowest element
        i = low #make i and j pointer at the two extreme points and compare them 
        j = high  

        while(i<j): #till i crosses j or vice versa
            #check if value at i position is greater than the value at pivot if yes then stop incrementing i otherwise move it to right
            while(arr[i] <= pivot and i <= high-1):
                i += 1
            #check if value at j position is less than value at pivot if yes then stop otherwise move it to left
            while(arr[j] > pivot and j >= low+1 ):
                j -= 1

            #Now we have found the value from i and j now swap both the values
            if i < j:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

        #Now swap the pivot element with the j th element to fix it at correct position
        temp2 = arr[j]
        arr[j] = arr[low]
        arr[low] = temp2   
        return j

    
    def qsort(self, nums, low, high):
        if low < high:
            pindex = self.fixpivot(nums, low, high)
            self.qsort(nums, low, pindex - 1)
            self.qsort(nums, pindex + 1, high)


    def quickSort(self, nums):
        low = 0
        high = len(nums)-1
        self.qsort(nums, low, high)
        return nums


obj = Solution()

print(obj.quickSort([4,1,9,10,7,2,3]))