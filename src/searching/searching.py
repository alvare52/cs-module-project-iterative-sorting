def linear_search(arr, target):
    # Your code here

    for i in range(0, len(arr)):
        print(arr[i])
        if arr[i] == target:
            print("Found!")
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    last = (len(arr) - 1)

    found = False
    found_index = -1

    while first <= last and not found:
        middle = (first + last) // 2

        if arr[middle] == target:
            found_index = middle
            found = True

        else: 
            if target < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found_index
