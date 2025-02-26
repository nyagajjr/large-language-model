# Doublng each elements in an array

def double(numbers):
    result = numbers.copy()
    for elem in range(len(result)):
        result[elem] *= 2
    return result

print(double([1, 2, 3, 4, 5]))
