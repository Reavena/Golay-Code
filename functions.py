

def identity_matrix(n):
    """
    Generate an n x n identity matrix.
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
  
def add_matrices(A, B):
    """
    Add two matrices of the same dimensions.
    """
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j] % 2)
        result.append(row)
    return result

def multiply_matrices(A, B):
    """
    Multiply matrix A (m x n) with matrix B (n x p).
    """
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            sum_val = 0
            for k in range(n):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val % 2)
        result.append(row )
    return result

def h_stack(A, B):
    """
    Horizontally stack two matrices.
    """
    if len(A) != len(B):
        raise ValueError("Matrices must have the same number of rows for h_stack.")
    return [A[i] + B[i] for i in range(len(A))]

def v_stack(A, B):
    """
    Vertically stack two matrices.
    """
    if len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same number of columns for v_stack.")
    return A + B