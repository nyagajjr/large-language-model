def palindrome(pal):
    low = 0
    high = len(pal) - 1
    while low < high:
        if pal[low] != pal[high]:
            return "Not Palindrome"
        else:
            low += 1
            high -= 1
    return "Palindrome detected"

        

print(palindrome("mom"))
print(palindrome("abca"))
