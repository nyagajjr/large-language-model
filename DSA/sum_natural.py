# Given a number n, find the sum of the first natural numbers.

# Examples : 

# Input: n = 3
# Output: 6
# Explanation: Note that 1 + 2 + 3 = 6

# Input  : 5
# Output : 15 
# Explanation : Note that 1 + 2 + 3 + 4 + 5 = 15

def sum_natural(n):
    counter = 0
    for i in range(1, n+1):
        counter += i
    return counter

print(sum_natural(52345675))

