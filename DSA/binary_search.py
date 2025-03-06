#A binary search algortihm

def binary_search(arr, item):
    low = 0 
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 10, 11, 20, 25]
print(binary_search(my_list, 3)) # => 1 
print(binary_search(my_list, -1)) # => None
print(binary_search(my_list, 10)) # => 5
print(binary_search(my_list, 20)) # => 7

