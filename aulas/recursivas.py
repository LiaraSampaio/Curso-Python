# Funções recursivas e recursividade

def recursiva(start=0, end=10):
    if start >= end:
        return end
    
    print(start, end)

    start += 1
    return recursiva(start, end)

print(recursiva())
print()


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(10))
