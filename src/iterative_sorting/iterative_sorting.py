# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    smallest_index = 0
    lowest = None
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # if right < left and not out of range
        if arr[cur_index] < arr[cur_index + 1] and (cur_index + 1) < len(arr):
        # (hint, can do in 3 loc)
        # Your code here
            smallest_index = cur_index
            lowest = arr[cur_index]

        # TO-DO: swap
        # Your code here
    old_first = arr[0]
    arr[0] = arr[smallest_index]
    arr[smallest_index] = old_first

    return arr

my_first_list = [4, 2, 7, 1, 5]
print(selection_sort(my_first_list))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    has_swapped = True
    turn = 0
    while has_swapped:
        turn += 1
        has_swapped = False
        # print(f"turn: {turn}")
        # loop through everything in array
        for x in range(0, len(arr) - 1):
            # print(x)
            # left > right
            if arr[x] > arr[x + 1] and x + 1 < (len(arr)):
                temp = arr[x + 1] # right
                arr[x + 1] = arr[x] # right is now left
                arr[x] = temp # old left is now right
                has_swapped = True
                # print(f"left: {arr[x + 1]},right:{arr[x]}")

    print(f"total turns: {turn}")
    print(f"array now: {arr}")
    return arr

# my_list = [1, 5, 4, 7, 2, 3]
# print(bubble_sort(my_list))

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

def insertion_sort(input_list):

    # mark first item as sorted (no code needed, just conceptual)
    # for every item starting at the second element
    for i in range(1, len(input_list)):
        # put current item in temp variable
        current_item = input_list[i]
        
        look_left_index = i - 1

        # look left, until we find where it belongs
        # if we are not at the beginning
        # and current item is less than sorted
        while look_left_index > 0 and current_item < input_list[look_left_index]:
            input_list[look_left_index + 1] = input_list[look_left_index]
            look_left_index -= 1
        
        input_list[look_left_index] = current_item
    return input_list