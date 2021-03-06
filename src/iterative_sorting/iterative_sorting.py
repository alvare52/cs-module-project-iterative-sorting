# TO-DO: Complete the selection_sort() function below
# O(n^2) - not good
def selection_sort(arr):

    # loop through array and find smallest element
    for i in range(len(arr)):

        # just pick first index for now
        smallest = i

        for j in range(i + 1, len(arr)):
            
            # if we find anything smaller that the starting one, change it
            if arr[smallest] > arr[j]:
                smallest = j

        # Swap first element with the smallest
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        # shorthand for swapping 
        # arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr

my_first_list = [4, 2, 7, 1, 5]
print(selection_sort(my_first_list))

# TO-DO:  implement the Bubble Sort function below
# O(n^2) - not good
def bubble_sort(arr):
    # Your code here
    has_swapped = True
    turn = 0
    while has_swapped:
        turn += 1
        has_swapped = False

        # loop through everything in array
        for x in range(0, len(arr) - 1):
            
            # left > right
            if arr[x] > arr[x + 1] and x + 1 < (len(arr)):
                temp = arr[x + 1] # right
                arr[x + 1] = arr[x] # right is now left
                arr[x] = temp # old left is now right
                has_swapped = True

    print(f"total turns: {turn}")
    print(f"array now: {arr}")
    return arr

my_list2 = [1, 5, 4, 7, 2, 3]
print(bubble_sort(my_list2))

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
def count_sort(arr, maximum=None):
    # Your code here
    if len(arr) < 1:
        return []
        
    max_element = int(max(arr)) 
    # max_element = maximum

    min_element = int(min(arr)) 
    range_of_elements = (max_element - min_element) + 1
    # Create a count array to store count of individual 
    # elements and initialize count array as 0 
    count_arr = [0 for _ in range(range_of_elements)] 
    output_arr = [0 for _ in range(len(arr))] 
  
    # Store count of each character 
    for i in range(0, len(arr)): 
        count_arr[arr[i]-min_element] += 1
  
    # Change count_arr[i] so that count_arr[i] now contains actual 
    # position of this element in output array 
    for i in range(1, len(count_arr)): 
        count_arr[i] += count_arr[i-1] 
  
    # Build the output character array 
    for i in range(len(arr)-1, -1, -1): 
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
        count_arr[arr[i] - min_element] -= 1
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(0, len(arr)): 
        arr[i] = output_arr[i] 

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


# my_test = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# new_list = []
# for element in my_test:
#     if element % 3 == 0:
#         print(element)
# #         new_list.append(element)

# # for element in new_list:
# #     print(element)
# # print(new_list)