def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    Args:
    - triangle: A list of lists representing Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
    - n: Number of rows to generate.

    Returns:
    - A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return (triangle)


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

