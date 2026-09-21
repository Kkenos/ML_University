
n = int(input("quatity: "))


numbers = [int(x) for x in input("input: ").split()[:n]]


original_numbers = numbers.copy()


if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]


print("list:", original_numbers)
print("udated list:", numbers)