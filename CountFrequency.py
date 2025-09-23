# def countFreq(num, freqmap):
#     return freqmap[num]

# arr = [10,5,10,15,10,5]
# freqmap = {}
# #Precompute the hash
# for i in arr:
#     if i in freqmap:
#         freqmap[i] += 1
#     else:
#         freqmap[i] = 1

# print(countFreq(5, freqmap))

def count_frequencies(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

arr = [10, 5, 10, 15, 10, 5]
print(count_frequencies(arr))   # {10: 3, 5: 2, 15: 1}
