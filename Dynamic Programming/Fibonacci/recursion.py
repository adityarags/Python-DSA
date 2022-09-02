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
