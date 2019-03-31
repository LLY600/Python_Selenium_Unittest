#冒泡
def bobble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bobble_sort([1,4,2,5]))

#插入
def  insert_sort(arr):
    length = len(arr)
    i = 1
    while i < length:
        j = i
        while j > 0:
            if arr[j-1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -=1
        i += 1
    return arr
print(insert_sort([1,9,6,5]))

