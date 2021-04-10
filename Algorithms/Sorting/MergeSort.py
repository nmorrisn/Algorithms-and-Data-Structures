def merge_sort(arr):
    if len(arr) == 1:
        return arr

    # Split up array
    mid = int(len(arr)/2)

    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    # compare left and right and zip them up
    arr = []
    j = 0
    k = 0
    while k < len(right) or j < len(left):
        if k >= len(right) or (j < len(left) and left[j] < right[k]):
            arr.append(left[j])
            j += 1
        else:
            arr.append(right[k])
            k += 1

    return arr





numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(numbers))