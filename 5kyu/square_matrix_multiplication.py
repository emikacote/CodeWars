def matrix_mult(mat1, mat2):
    ans = [[0 for i in range(len(mat1))] for j in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1)): ans[i][j] += mat1[i][k]*mat2[k][j]
    return ans
  
# or  

def matrix_mult(a, b):
    l = range(len(a))
    return [[sum(a[i][k]*b[k][j] for k in l) for j in l] for i in l]
