def generate_series_modified(n):
    series = []
    for i in range(1, n+1, 2):
        series.append(i)
    if n % 2 == 0:
        series = series[:-1]
    return series


a = int(input("Enter a number: "))
print(generate_series_modified(a))
