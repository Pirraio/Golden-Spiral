def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

num = int(input())
for i in range(num):
    print(f'{fibonacci(i+1)}', end=' ')