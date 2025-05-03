'''print matrix row by row:'''

def row_by_row(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

print('''\nprint matrix row by row:''')
row_by_row(matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
])


'''\nPrint only the first column:'''

def first_col(matrix):
    for i in range(len(matrix)):
        print(matrix[i][0], end="\n")

print('''\nPrint only the first column:''')
first_col(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

'''opp_diag_sum of all elements'''

def matrix_sum(matrix):
    total=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total+=matrix[i][j]
    print(total)

print('''\nsum of all elements''')
matrix_sum(matrix = [
    [5, 5],
    [5, 5]
])

'''largest element'''

def largest(matrix):
    track=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            track=max(track,matrix[i][j])
    print(track)

print('''\nlargest element''')
largest(matrix = [
    [1, 99, 3],
    [88, 5, 6],
    [7, 8, 100]
])

'''print diagonal elements'''

def diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                print(matrix[j][i],end='\n')

print('''\nprint diagonal elements''')
diagonal(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

'''print matrix row by row in reverse'''
def rev_row(matrix):
    n=len(matrix)-1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[n-i][j], end=" ")
        print(" ")

print('''\nprint matrix row by row in reverse''')
rev_row(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]
])

'''Print the matrix column by column, top to bottom (normal), but after finishing, reverse the columns printed'''
def rev_col(matrix):
    n=len(matrix)-1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[j][i], end="\n")
        print(" ")
    print("\nNow reverse columns:\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[n-j][n-i], end="\n")
        print(" ")


print('''\nprint matrix col by col in reverse''')
rev_col(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

'''opp_diag_sum of opp diagonal elements'''
def opposite_diagonal_sum(matrix):
    n = len(matrix)
    opp_diag_sum=0
    # i+j=n-1 => j=n-1-i
    for i in range(n):
        if i == n - 1 - i :
            opp_diag_sum+=matrix[i][n - 1 - i]
    print(opp_diag_sum)

print('''\nSum of opp diagonal elements''')
opposite_diagonal_sum(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

'''Check if matrix is square or not'''
def is_square(matrix):
    if len(matrix) == len(matrix[0]):   # if row==col, matrix is square
        print(True)
    else:
        print(False)

print('''\nCheck if matrix is square or not''')
is_square(matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


'''Transpose'''
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(cols):
        for j in range(rows):
            print(matrix[j][i], end=" ")
        print()

print('''\nTranspose''')
transpose(matrix = [
 [1,2,3],
 [4,5,6]
])
