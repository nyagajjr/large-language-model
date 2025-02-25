def solution(A):
    A = sorted(A)
    size = len(A)
    if not A:
        return None
    for i in range(1, size + 1):
        if i not in A:
            return i
        
print(solution([2,4,3,1]))