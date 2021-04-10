def selectsort(arr):
    # loop through the array and fin the minimum value
    # swap it with the first item
    # starting with the second item, run through the list again
    min_index = -1
    for i in range(len(arr)):
        min_index = -1
        for j in range(i, len(arr)):
            if min_index == -1 or arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [2, 3, 1, 20, 4, 8, -1, 400, -2]
selectsort(arr)
print(arr)
