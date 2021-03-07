"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    i, y = 0, 0
    while (y < len(matrix)):
        if (i == 4):
            break
        print("%.2f" % float(matrix[y][i]), end = '\t')
        y += 1
        if (y == len(matrix)):
            print("")
            y = 0
            i += 1

#turn the parameter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(4):
        for y in range(len(matrix[0])):
            if (x == y):
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = new_matrix(cols = len(m2))
    for x in range(len(m2)):
        for y in range(4):
            temp[x][y] = m1[y][0] * m2[x][0] + m1[y][1] * m2[x][1] + m1[y][2] * m2[x][2] + m1[y][3] * m2[x][3]
    m2 = temp
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m