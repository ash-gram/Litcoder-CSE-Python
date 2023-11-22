def lastRemaining( n):
    if n == 1:
        return 1
    return 2*(n//2 +1 - lastRemaining(n//2))

inp = int(input())
print(lastRemaining(inp))