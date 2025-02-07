# Given a number n, check whether it is even or odd. Return true for even and false for odd.

# Examples: 
# Input: 2 
# Output: true
# Input: 5
# Output: false

def num(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(num(28))
print(num(7))
