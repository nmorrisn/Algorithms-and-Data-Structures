def sort_bit_array(arr):
    # need to sort an array of 1's and 0's using a hash table
    # linear time, do not use multiple pointers, comparison sort, etc.
    # sort in place
    # loop through the array and count up the 0's and 1's
    # loop through array again and replace with 0's until count is 0
    # continue looping and replace with 1's
    count = {0: 0, 1: 0}
    for num in arr:
        count[num] += 1

    for i in range(len(arr)):
        if count[0] > 0:
            arr[i] = 0
            count[0] -= 1
        else:
            arr[i] = 1   


arr = [0, 1, 1, 0, 1, 1, 1, 0]
sort_bit_array(arr)
print(arr)