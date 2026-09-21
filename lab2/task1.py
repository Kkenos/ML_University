bukvi = ['a','b','c','d','e','f']
cifri = [1,2,3,4,5]

slovar = dict(zip(bukvi,cifri))

print(slovar)

total_sum = sum(slovar.values())

print("Сумма всех значений:", total_sum)

with open("file-1.txt", "w", encoding="utf-8") as file:
    file.write(str(total_sum))