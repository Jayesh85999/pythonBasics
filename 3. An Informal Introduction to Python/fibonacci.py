0, 1, 1, 2, 3, 5, 8, 13

firstTerm = 0
secondTerm = 1


def fib(n):
    firstTerm = 0
    secondTerm = 1

    i = 2
    current = 0
    while i <= n:
        current = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = current
        i = i + 1

    return current


x = fib(7)
print(x)
