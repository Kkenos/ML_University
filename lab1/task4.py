def sum_1(n: int) -> float:
    
    return sum(1 / (i ** 2) for i in range(1, n + 1))


def sum_2(n: int, m: int) -> int:
    
    return sum(i ** n for i in range(1, m + 1))




result_1 = sum_1(3)
print("Результат sum_1(n=3):", result_1)



result_2 = sum_2(2, 4)
print("Результат sum_2(n=2, m=4):", result_2)