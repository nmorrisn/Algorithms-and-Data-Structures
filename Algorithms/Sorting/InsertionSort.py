def insertsort(arr):
    # loop through our array and insert values into another array
    # for each value in arr we loop through our other array and see where we should put it
    # then we need to swap values to put it in the correct place
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Function to do insertion sort
def insertionSort(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


arr = [2, 3, 1, 20, 4, 8, -1, 400, -2]
insertsort(arr)

print(arr)

        
        