def find_median(lst):
    if not lst:
        raise ValueError("Empty list")
    lst.sort()  # Sort the list
    n = len(lst)
    print(n)
    mid = n // 2
    print(mid)
    print(lst[mid])

    if n % 2 == 0:
        return (lst[mid] + lst[mid-1]) / 2  # Average of middle two
    else:
        return lst[mid]  # Middle element

my_list = []
print(find_median(my_list)) 