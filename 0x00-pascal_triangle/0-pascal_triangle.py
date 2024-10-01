def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of 1's
        for j in range(1, i):  # Calculate the values in the middle
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

# Example usage:
result = pascal_triangle(5)
print(result
     )
