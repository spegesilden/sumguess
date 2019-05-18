def fac(n):
    if n < 2:
        return 1
    return n * fac(n - 1)

def binomial(n, k):
    a = fac(n)
    b = fac(k) * fac(n - k)

    return float(a/b)

def expectedValue(n):
    a = 0
    b = 6 ** n
    print(n, b)

    for i in range(n, n*6+1):
        a += i

    return float(a/b)

print(expectedValue(2))
