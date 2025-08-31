def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        result[i] = sum(1 for num in numbers if num % i == 0)
    return result


nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(nums))
