# sort an array from smallest to largest. 
# Let’s write a function to find the smallest element in an array:
def find_smallest(arr):
    smallest = arr[0] 
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i # 3
    return smallest_index

## slection sort
def selection_sort(arr):
    new_arr = []
    copied_arr = list(arr) # copy arr before mutating
    print(copied_arr)
    for i in range(len(copied_arr)):
        smallest = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))