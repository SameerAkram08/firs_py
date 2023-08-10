# a = [[1,3],
#      [2,3]]

# b = [[3,4],
#      [4,5]]    

# c = [[0,0],
#      [0,0]]

# if len(a)==len(b):
  
#   for i in range( 0 ,len(c)):
#       for j in range(0,len(c[0])):
#           for k in range(0,len(c)):
#               c[i][j] =  a[i][k]* b[k][j]
  
#   for row in c:
#       print(row)            
  
# else:
#     print("dimentions are not equal")


def get_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i}, {j}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Get dimensions of the matrices from the user
rows_a = int(input("Enter the number of rows for matrix A: "))
cols_a = int(input("Enter the number of columns for matrix A: "))

rows_b = int(input("Enter the number of rows for matrix B: "))
cols_b = int(input("Enter the number of columns for matrix B: "))

# Check if matrices are compatible for multiplication
if cols_a == rows_b:
    print("Enter elements for matrix A:")
    matrix_a = get_matrix_input(rows_a, cols_a)
    
    print("Enter elements for matrix B:")
    matrix_b = get_matrix_input(rows_b, cols_b)
    
    matrix_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    print("Resultant matrix C:")
    print_matrix(matrix_c)
else:
    print("Dimensions are not compatible for multiplication.")
