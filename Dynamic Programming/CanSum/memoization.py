def canSum(n, a, memo = {}):
    if n in memo:
        return memo[n]
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        for i in a:
            
            memo[n - i] = canSum(n - i, a, memo)
            if memo[n - i]:
                return True
    return False

print(canSum(7, [2, 3, 4, 5, 7]))
print(canSum(5, [2, 7]))
print(canSum(3000, [7, 14]))