# Finding the nth fibonacci number by using Memoization(Dynamic Programming)
def Memofib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        memo[n] = Memofib(n - 1) + Memofib(n - 2)
        return memo[n]

print("Memoization Fibonacci")
print(Memofib(5))   # Shows output "5" Quickly
print(Memofib(10))  # Shows output "55" Quickly
print(Memofib(50))  # Shows output "12586269025" immediately