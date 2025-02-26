numbers = [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 9, 10, 10, 10]

print(len(numbers)) # -- prints the number of items in the list

print(numbers.index(4)) # prints out the index of 4

print(numbers.count(10)) # Counts teh number of occurrences of 10


numbers.append(5)
print(numbers) # [1, 2, 3, 4, 5]

numbers.insert(1, 6)
print(numbers) # [1, 6, 2, 3, 4, 5]

#copying the elements in a new variable
b = numbers.copy()

numbers.append(20)

print(numbers)
print(b)