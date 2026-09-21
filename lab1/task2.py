numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]


min_abs = min(numbers, key=abs)

max_abs = max(numbers, key=abs)

sorted_by_abs = sorted(numbers, key=abs)

print("min", min_abs)
print("max", max_abs)
print("sorted mass", sorted_by_abs)

