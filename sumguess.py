def fac(n):
    if n < 2:
        return 1
    return n * fac(n - 1)

def binomial(n, k):
    a = fac(n)
    b = fac(k) * fac(n - k)

    return float(a/b)

def generateRolls(n, V):
    if n == 0:
        return V

    R = []
    V2 = []

    for v in V:
        for i in range(1, 7):
            v2 = v[::]
            v2.append(i)
            V2.append(v2)
        R.append(v)

    for r in R:
        V.remove(r)

    for v in V2:
        V.append(v)

    return generateRolls(n - 1, V)


def expectedValue(n, N):
    a = 0
    b = 6 ** n

    for n in N:
        for i in n:
            a += i

    return float(a/b)

V = generateRolls(1, [[i] for i in range(1, 7)])
print(1, expectedValue(1, V))

for i in range(1,10):
    V = generateRolls(1, V)
    print(1 + i, expectedValue(1 + i, V))
