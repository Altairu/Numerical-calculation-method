import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    
    # 前進消去を行う
    for i in range(n):
        pivot = A[i, i]                 # 対角成分をpivotに代入
        A[i] = A[i] / pivot             # pivotで係数行列を割り、A[i,i]を1にする
        b[i] = b[i] / pivot             # 定数ベクトルもpivotで割り同値変形する
        print(f"Step {i+1} - Normalize row {i}:\nA =\n{A}\nb = {b}\n")

        # i行目の定数倍をi+1行目以降から引くループ
        for j in range(i+1, n):
            p = A[j, i]                 # i+1行目以降i列の数値を格納
            A[j] -= p * A[i]            # 係数行列のi+1行目からi行目の定数倍を引く
            b[j] -= p * b[i]            # 定数ベクトルのi+1行目からi行目の定数倍を引く
            print(f"Step {i+1} - Eliminate row {j} using row {i}:\nA =\n{A}\nb = {b}\n")

    # 後退代入を行う
    x = np.zeros(n)                     # 解の入れ物を用意
    for i in reversed(range(n)):        # 最終行から後退処理する
        x[i] = b[i] / A[i, i]           # 解を求める
        for j in range(i):
            b[j] -= A[j, i] * x[i]      # 解が求まった列分bの値を上から更新する
        print(f"Step {n+i+1} - Back substitution for row {i}:\nx = {x}\nb = {b}\n")
    return x

# 係数行列(n次正方行列であること)
A = np.array([
    [1, -1, -2],
    [0, -3, 2],
    [4, 1, -2]], dtype=float)

# 定数ベクトル
b = np.array([5, 4, 4], dtype=float)

# ガウスの消去法関数を実行して解を得る
x = gaussian_elimination(A, b)
print("Solution:\n", x)
