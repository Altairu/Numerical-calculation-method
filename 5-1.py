import numpy as np

# 拡大係数行列の作成
A = np.array([
    [0, -3, 2, 4],
    [1, -1, -2, 5],
    [4, 1, -2, 4]
], dtype=float)

def gauss_elimination(A):
    n = len(A)
    
    # 前進消去操作
    for i in range(n):
        # 部分ピボット操作（最大絶対値の行を探して入れ替え）
        max_row = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        print(f"Step {i+1}: Pivot row swapping")
        print(A)
        
        # ピボット行の正規化
        A[i] = A[i] / A[i, i]
        print(f"Step {i+1}: Pivot row normalization")
        print(A)
        
        # 他の行を消去
        for j in range(i+1, n):
            A[j] = A[j] - A[i] * A[j, i]
            print(f"Step {i+1}.{j+1}: Eliminate row {j+1}")
            print(A)

    # 逆進代入操作
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = A[i, -1] - np.dot(A[i, i+1:n], x[i+1:n])
        print(f"Step {n+i+1}: Back substitution for x[{i}]")
        print(f"x[{i}] = {x[i]}")
    
    return x

# ガウス消去法の実行
solution = gauss_elimination(A)

# 結果の表示
print("解: ", solution)
