def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        row_before = triangle[i - 1]

        for j in range(1, i):
            row.append(row_before[j - 1] + row_before[j])

        row.append(1)
        triangle.append(row)

    return triangle