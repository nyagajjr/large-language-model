# Sum of Digits of a Number
# Given a number n, find the sum of its digits.

# Examples : 

# Input: n = 687
# Output: 21
# Explanation: The sum of its digits are: 6 + 8 + 7 = 21


# Input: n = 12
# Output: 3
# Explanation: The sum of its digits are: 1 + 2 = 3

def num(n):
    stringer = str(n)
    lst = []
    counter = 0
    for i in stringer:
        lst.append(int(i))
    for i in lst:
        counter += i
    return counter

print(num(687))