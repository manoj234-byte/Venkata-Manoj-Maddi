def series(a):
    if a <= 0:
        return []

    series = []
    for i in range(1, a + 1):
        if i % 2 != 0:
            series.append(i)

    return series

print(series(int(input("n: "))))
