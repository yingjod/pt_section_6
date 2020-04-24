def compute(mat, num_row, num_col):
    for i in range(num_row):
        for j in range(num_col):
            print("%d" % mat[i][j], end=" ")
        print()


rows = cols = 2
mat1 = []
mat2 = []

print("enter matrix 1 :")
for i in range(rows):
    mat1.append([])
    for j in range(cols):
        print("[%d,%d]: " % (i + 1, j + 1), end="")
        mat1[i].append(eval(input()))

print("enter matrix 2 :")
for i in range(rows):
    mat2.append([])
    for j in range(cols):
        print("[%d,%d]: " % (i + 1, j + 1), end="")
        mat2[i].append(eval(input()))
print("matrix 1 :")
compute(mat1, rows, cols)
print("matrix 2 :")
compute(mat2, rows, cols)

print("sum of 2 matrices:")
for i in range(rows):
    for j in range(cols):
        print("%d" % (mat1[i][j] + mat2[i][j]), end=" ")
    print()
