# As a part of this Kata, you need to create a function that when provided with a triplet, 
# returns the index of the numerical element that lies between the other two elements.

# The input to the function will be an array of three distinct numbers (Haskell: a tuple).

# For example:

# print(gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

# Another example (just to make sure it is clear):

# gimme([5, 10, 14]) => 1

def gimme(arr):
    sort = sorted(arr)
    arr_range = range(len(arr))
    for i in arr_range:
        if sort[1] == arr[i]:
            return i
        
print(gimme([2, 3, 1])) #--> 0
print(gimme([5, 10, 14])) #--> 1
print(gimme([1, 3, 2])) #--> 2
print(gimme([52, 104, 140])) #--> 1

#OR

def gimme_short(arr):
    return arr.index(sorted(arr)[1])

print(gimme_short([2, 3, 1])) #--> 0
print(gimme_short([5, 10, 14])) #--> 1
print(gimme_short([1, 3, 2])) #--> 2
print(gimme_short([52, 104, 140])) #--> 1