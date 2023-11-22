def clumsy(n):
    op = 0
    num = n
    for i in range(n-1, 0, -1):
        if op == 0:
            num *= i
        elif op == 1:
            num //= i
        elif op == 2:
            num += i
        elif op == 3:
            num -= i
        op = (op + 1) % 4
    return num

inp = int(input())
print(clumsy(inp))
