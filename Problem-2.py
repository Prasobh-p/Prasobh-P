def generate_series(n):
    series = [2*i + 1 for i in range(n)]
    return series


a = int(input("Enter a number: "))
print(generate_series(a))
