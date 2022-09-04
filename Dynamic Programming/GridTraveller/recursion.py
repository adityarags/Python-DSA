def gridTravel(m, n):
    if m == n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        return gridTravel(m - 1, n) + gridTravel(m , n - 1)
    
# print(gridTravel(3, 4))