def bubble(arr):
    # implement bubble sort
    # loop through the array and do pair wise comparisons
    # if the pair is not ordered correctly, swap them in place
    # for each loop, go one less index
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble([2, 3, 1, 20, 4, 8]))