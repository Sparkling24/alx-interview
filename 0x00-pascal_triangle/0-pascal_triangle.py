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

# Example usage:
print(pascal_triangle(5))



#def pascal_triangle(n):
   # if n <= 0:
    #    return []
    
  #  triangle = []
    
   # for i in range(n):
       # row = [1] * (i + 1)  # Start with a row of 1's
     #   for j in range(1, i):  # Calculate the values in the middle
       #     row[j] = triangle[i-1][j-1] + triangle[i-1][j]
      #  triangle.append(row)
    
  #  return triangle

# Example usage:
#result = pascal_triangle(5)
#print(result
     )



#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


#def pascal_triangl(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
  #  res = []
  #  if n > 0:
   #     for i in range(1, n + 1):
          #  level = []
         #   C = 1
         #   for j in range(1, i + 1):
          #      level.append(C)
           #     C = C * (i - j) // j
          #  res.append(level)
   # return re
