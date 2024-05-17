import numpy as np

# 拡大係数行列の作成
A = np.array([
    [0, -3, 2, 4],
    [1, -1, -2, 5],
    [4, 1, -2, 4]
], dtype=float)

def gauss_jordan_elimination(A):
    n = len(A)
    
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
        
        # 前進消去操作
        for j in range(n):
            if i != j:
                A[j] = A[j] - A[i] * A[j, i]
                print(f"Step {i+1}.{j+1}: Eliminate row {j+1}")
                print(A)

    # 解の抽出
    x = A[:, -1]
    
    return x

# ガウス・ジョルダン消去法の実行
solution = gauss_jordan_elimination(A)

# 結果の表示
print("解: ", solution)
