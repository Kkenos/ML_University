import math

def calculate_rectangle_area(width: float, height: float) -> float:

    return width * height

def calculate_circle_area(radius: float) -> float:

    return math.pi * (radius ** 2)

def is_prime(number: int) -> bool:

    if number <= 1:
        return False
    for i in range(2, int(math.isqrt(number)) + 1):
        if number % i == 0:
            return False
    return True