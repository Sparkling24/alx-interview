#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangl
e
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
                                                 if __name__ == "__main__":                                          print_triangle(pascal_triangle(5))
define pascal_triangle(n)
       a=[[] for i in range(n)]
       for i in range(n):
       for j in range(i+1):
           if(j<i):
               if (j==0):
                   a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif(j==i):
                a[i].append(1)
        return a
n=5
print(pascal_triangle(n)
