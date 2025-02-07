# Given two numbers a and b, the task is to swap them.

# Examples:

# Input: a = 2, b = 3
# Output: a = 3, b = 2

# Input: a = 20, b = 0
# Output: a = 0, b = 20

# Input: a = 10, b = 10
# Output: a = 10, b = 10 
2,3
def swap(a,b):
    # c=a 
    # a=b
    # b=c
    a,b = b,a #tuple unpacking
    return a,b

print(swap(2,3))

