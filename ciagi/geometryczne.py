def nwyrazq(a1, q, n):
    return a1 * q ** (n - 1)


def sumanwyrazow(a1, q, n):
    if q == 1:
        return a1 * n
    return a1 * ((1 - q ** n) / (1 - q))