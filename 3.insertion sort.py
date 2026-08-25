def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

arr = [2,6,7,4,3,1]
print("Before Sorting:",arr)    
print("After Sorting:",bubble_sort(arr))