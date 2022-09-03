def canSum(n, a):
    if n < 0:
        return False
    if n == 0:
        return True
    for i in a:
        if canSum(n - i, a):
            return True
    return False

print(canSum(7, [2, 3, 4, 5, 7]))
print(canSum(5, [2, 7]))
print(canSum(3000, [7, 14]))