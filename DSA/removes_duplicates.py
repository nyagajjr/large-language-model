#If you must maintain the order of occurrence
def remove_duplicates(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

print(remove_duplicates([70, 10, 20, 20, 30, 30, 30, 40, 50, 50])) 

#Better efficiency
def remove_duplicates(nums):
    return list(dict.fromkeys(nums))


