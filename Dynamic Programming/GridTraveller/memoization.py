def gridTravel(m, n, memo = {}):
    key = (m,n)
    if key in memo:
        return memo[key]
    if m == n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        memo[key] = gridTravel(m - 1, n, memo) + gridTravel(m , n - 1, memo)
        return memo[key]    
print(gridTravel(3, 3))
print(gridTravel(18,18))