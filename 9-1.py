import numpy as np

# 標本点
points = [(-1, 3), (0, 1), (1, 1), (2, 9)]

# ラグランジュ補間多項式を計算する関数
def lagrange_interpolation(x, points):
    total = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if i != j:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        total += term
    return total

# x = 1.5 における y の値を計算
x_value = 1.5
y_value = lagrange_interpolation(x_value, points)
print (y_value)