rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input())
        row.append(val)
    matrix.append(row)

print("\nMatrix you entered:")
for r in matrix:
    print(r)

results = []

if rows == cols:
    is_upper = True
    for i in range(rows):
        for j in range(i):
            if matrix[i][j] != 0:
                is_upper = False
    if is_upper:
        results.append("Upper Triangular Matrix")

    is_lower = True
    for i in range(rows):
        for j in range(i+1, cols):
            if matrix[i][j] != 0:
                is_lower = False
    if is_lower:
        results.append("Lower Triangular Matrix")

    is_diagonal = True
    for i in range(rows):
        for j in range(cols):
            if i != j and matrix[i][j] != 0:
                is_diagonal = False
    if is_diagonal:
        results.append("Diagonal Matrix")

        first_val = matrix[0][0]
        is_scalar = True
        for i in range(rows):
            if matrix[i][i] != first_val:
                is_scalar = False
        if is_scalar:
            results.append("Scalar Matrix")

            if first_val == 1:
                results.append("Identity Matrix")
else:
    results.append("Not a square matrix, so cannot be triangular/diagonal/scalar/identity")

print("\nMatrix Type(s):")
for r in results:
    print("-", r)
