def isSoDep(n):
    a = str(n)
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True
n=int(input())
result= isSoDep(n)
print(result)