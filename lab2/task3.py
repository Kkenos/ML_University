file_name = "z3.1-11.txt"


with open(file_name, "r", encoding="utf-8") as file:
    content = file.read().strip()


numbers = list(map(int, content.split()))


total_sum = sum(numbers)


print("Сумма чисел:", total_sum)


with open(file_name, "a", encoding="utf-8") as file:
    file.write(f"\n{total_sum}")