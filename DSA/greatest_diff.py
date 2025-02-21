# Let us consider a task, where we are given a list of numbers, 
# and the goal is to find the largest difference between any two numbers. For example, 
# when the list is [3, 2, 6, 5, 8, 5], the desired answer is 6, because the largest difference is between the numbers 2 and 8.

def diff(arr):
    new__arr = sorted(arr)
    return new__arr[-1] - new__arr[0]

print(diff([3, 2, 6, 5, 8, 5]))