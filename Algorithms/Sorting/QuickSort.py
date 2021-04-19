# optimization is to grab three elements and grab the median
# three could be three random, or the beginning/middle/end
# random might be the best

def quicksort(instr):
    
    def subsort(arr):
        if len(arr) < 2:
            return arr

        lesser = []
        greater = []

        pivot = arr[len(arr)-1]

        for i in range(len(arr)-1):
            if arr[i] < pivot:
                lesser.append(arr[i])
            else:
                greater.append(arr[i])

        return subsort(lesser) + [pivot] + subsort(greater)

    return subsort(instr)

def quicksort_ip(arr):
    
    def subsort(left, right):
        nonlocal arr
        if left >= right:
            return

        i = left
        w = left
        pivot = right

        while i < right:
            if arr[i] < arr[pivot]:
                arr[i], arr[w] = arr[w], arr[i]
                i += 1
                w += 1
            else:
                i += 1

        arr[w], arr[pivot] = arr[pivot], arr[w]

        subsort(left, w-1)
        subsort(w+1, right)
        

    subsort(0,len(arr)-1)
    return arr


print(quicksort([3,1,9,4,3,2,19,29,10]))
print(quicksort_ip([3,1,9,4,3,2,19,29,10]))