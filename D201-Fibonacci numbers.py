#taking inputs
X = int(input())

fibonacciNumbers = [0, 1]
for i in range(2, X + 1):
    fibonacciNumbers.append(fibonacciNumbers[i - 1] + fibonacciNumbers[i - 2])

print(fibonacciNumbers[X])