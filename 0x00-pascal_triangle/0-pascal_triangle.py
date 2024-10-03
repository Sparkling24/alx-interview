#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        
        # Get the previous row
        previous_row = triangle[i - 1]
        
        # Generate the middle elements of the row
        for j in range(1, i):
            row.append(previous_row[j - 1] + previous_row[j])
        
        # End each row with 1
        row.append(1)
        
        # Append the new row to the triangle
        triangle.append(row)
    
    return triangle
