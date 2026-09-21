import random

def printMatrix(matrix):

    for row in matrix:
        for element in row:
            
            print("{:>4}".format(element), end="")
        print()  



N = int(input("количество строк (N): "))
M = int(input("количество столбцов (M): "))


matrix = [[random.randint(20, 80) for _ in range(M)] for _ in range(N)]

print("\nСгенерированный массив:")
printMatrix(matrix)