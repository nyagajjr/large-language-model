# Introduction to Primality Test and School Method
# Given a positive integer, check if the number is prime or not. 
# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# Examples of the first few prime numbers are {2, 3, 5, …}
# Examples : 


# Input:  n = 11
# Output: true


# Input:  n = 15
# Output: false


# Input:  n = 1
# Output: false

def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                return True
            
print(prime(23))