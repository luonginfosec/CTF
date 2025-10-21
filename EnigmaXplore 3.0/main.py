INIT = [0, 1, 1, 2, 3, 5, 8]  
C = [1, 1, 1, 1, 1, 1]  
def mat_multiply(A, B):
    """Multiply two matrices"""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Cannot multiply matrices")
    
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def mat_pow(matrix, power):
    if power == 0:
        n = len(matrix)
        identity = [[0] * n for _ in range(n)]
        for i in range(n):
            identity[i][i] = 1
        return identity
    
    if power == 1:
        return [row[:] for row in matrix]  # Deep copy
    
    if power % 2 == 0:
        half_pow = mat_pow(matrix, power // 2)
        return mat_multiply(half_pow, half_pow)
    else:
        return mat_multiply(matrix, mat_pow(matrix, power - 1))

def mat_vec(matrix, vector):
    result = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

def f_n(n: int) -> int:
    if n <= 0: 
        raise ValueError("n must be >= 1")
    if n <= 6: 
        return INIT[n]
    
    k = 6
    M = [C[:]] + [[0]*k for _ in range(k-1)]
    for i in range(1, k):
        M[i][i-1] = 1
    
    S = [INIT[6 - i] for i in range(k)]
    
    Mp = mat_pow(M, n - 6)
    return mat_vec(Mp, S)[0]

# Demo with test cases
if __name__ == "__main__":
    for i in range(1, 15):
        try:
            result = f_n(i)
            print(f"f_n({i}) = {result}")
        except Exception as e:
            print(f"Error for f_n({i}): {e}")

