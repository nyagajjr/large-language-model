# Let us consider an example, where the algorithm is given a list of numbers and the task is to count 
# how many of the numbers are even. 
# For example if the list is [5, 4, 1, 7, 9, 6], the desired answer is 2, because 4 and 6 are the even numbers.

# def even(lst):
#     evn = []
#     for i in lst:
#         if i % 2 == 0:
#             evn.append(i)

#     return len(evn)

# print(even([5, 4, 1, 7, 9, 6]))

def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

print(count_even([5, 4, 1, 7, 9, 6]))

