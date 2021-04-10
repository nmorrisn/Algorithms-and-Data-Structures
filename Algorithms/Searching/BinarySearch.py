def binsearch(arr, search):
    # given a sorted array
    # return the index of the search value
    # return None if it does not exist
    # what is the base case?
    # array length is 1
    if len(arr) == 1:
        return arr[0] == search

    mid = int(len(arr)/2)
    if search < arr[mid]:
        return binsearch(arr[:mid], search)
    else:
        return binsearch(arr[mid:], search)

def bsearch(arr, val):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = int((start + end)/2)
        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

nums = [1,3,4,5,6,7,8,10,11,13,15,17,20,22]
search = 8
print(bsearch(nums, search))