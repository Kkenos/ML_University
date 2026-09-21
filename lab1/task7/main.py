
from func import calculate_rectangle_area, calculate_circle_area, is_prime

w, h = 5.0, 10.0
rect_area = calculate_rectangle_area(w, h)
print(f"Площадь прямоугольника со сторонами {w} и {h}: {rect_area}")


r = 7.0
circle_area = calculate_circle_area(r)
print(f"Площадь круга с радиусом {r}: {circle_area:.2f}")

num = 29
if is_prime(num):
    print(f"Число {num} является простым.")
else:
    print(f"Число {num} НЕ является простым.")