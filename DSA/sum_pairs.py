# Check which pair gives the sum of a given number

def check_sum(arr, x):
    new_arr = []
    for i in arr:
        if (x - i) in new_arr:
            return True
        new_arr.append(i)
    return new_arr

print(check_sum([2, 4, 6, 9], 10))