#finding the nth fibonacci number using recursion
def fib(n):
    if (n <= 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print("Recursive Fibonacci")
print(fib(5))   # Shows output "5" Quickly
print(fib(10))  # Shows output "55" Quickly
# print(fib(50))  # Struggles to display the output



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