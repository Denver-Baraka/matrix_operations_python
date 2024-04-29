#input
#row echelon              .....
#reduced row echelon      .....
#gauss jordan
#determinant
#inverse

def row_echelon(matrix, variables, n_row, n_col):
	#find pivot -- largest item in the matrix
	pivot, row_poz, col_poz = largest_in_matrix(matrix, n_row, n_col)
	#swap rows or columns if necessary
	if row_poz != 0:
		swap_row(matrix, 0, row_poz)
		print("swapping rows")
	#if largest number is not in column 0 swap columns
	if col_poz != 0:
		swap_column(matrix, variables, 0, col_poz)
		print("swapping columns")
	#perform row reduction
	print("-------------------------------------------------------------------")
	print("the below matrix is now ready for row reduction")
	print_matrix(matrix, n_row, n_col)
	print("-------------------------------------------------------------------")
	row_reduction(matrix,n_row, n_col)
	return matrix

def reduced_row_echelon(newmatrix, n_row, n_col):
	#reduce pivots to 1
	for i in range(n_row):
		pivot = newmatrix[i][i]
		for j in range(n_col):
			newmatrix[i][j] = newmatrix[i][j] / pivot

	return newmatrix;

def largest_in_matrix(matrix, rowz, columnz):
	#slice the matrix
	temp_matrix = [row[:-1] for row in matrix]
	#find largest item in the sliced matrix
	largest_element = 0
	row_pos = 0
	col_pos = 0
	for row in temp_matrix:
		current=max(row)
		if current > largest_element:
			largest_element = current
			col_pos =row.index(largest_element)
			row_pos =temp_matrix.index(row)

	largest = [largest_element,row_pos, col_pos]
	return (largest_element,row_pos, col_pos)

def swap_row(matrix, row1, row2):
	temp = matrix[row1]
	matrix[row1] = matrix[row2]
	matrix[row2] = temp

def swap_column(matrix,variables, col1, col2):
	for row in matrix:
		temp = row[col1]
		row[col1] = row[col2]
		row[col2] = temp
	#swap variables
	tem = variables[col1]
	variables[col1] = variables[col2]
	variables[col2] = tem

def row_reduction(matrix,rowz,columnz):
	for row in range(rowz-1):
		pivot = matrix[row][row] 
		for j in range(row+1,rowz):
			if (matrix[j][row] != 0 and pivot != 0):
				multiplier = (matrix[j][row])/pivot
				for k in range(columnz):
					matrix[j][k] = round(((matrix[row][k] * multiplier * -1) + matrix[j][k]), 4)

def gauss_jordan(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        # Normalize the current row
        pivot = matrix[i][i]
        if pivot != 0:
            matrix[i] = [elem / pivot for elem in matrix[i]]

        # Eliminate the elements above and below the pivot
        for j in range(m):
            if i != j:
                factor = matrix[j][i]
                for k in range(n):
                    matrix[j][k] -= factor * matrix[i][k]

    return matrix

def print_matrix(matrix, n_row, n_col):
	rounded_matrix = [[None for _ in range(n_col)] for _ in range(n_row)]
	for i in range(n_row):
		for j in range(n_col):
			rounded_matrix[i][j] = round(matrix[i][j], 2)
	for row in rounded_matrix:
		print(row)
def num_solutions(matrix, n_row, n_col):
	for i in range(n_row):
		all_zero = 0
		for j in range(n_col - 1):
			if (matrix[i][j] == 0):
				all_zero = 0
			else:
				all_zero = 1
		if (all_zero == 0):
			if (matrix[i][n_col-1] == 0):
				#has many solutions
				print("error many solutions")
				return 0
			else:
				print("error no solution")
				return 1
def determinant(matrix):
	n = len(matrix)
	det = 1
	for i in range(n):
		det *= matrix[i][i]
	return round(det, 4)

def back_substitution(matrix, n_row, n_col):
	v = [1 for _ in range(n_col-1)]
	for i in range(n_row-1, -1, -1):
		sum = 0
		for j in range(n_col-3, i-1, -1):
			sum += (matrix[i][j+1] * v[j+1])
		value = (matrix[i][n_col-1] - sum)/matrix[i][i]
		v[i] = value
	
	return v



def input_matrix():
	m = int(input("   Enter the number of rows: "))
	n = int(input("Enter the number of columns: "))
	matrix = []
	print("Enter the elements row-wise:")
	for i in range(m):
		print(f"row {i}: ", end = '')
		row = list(map(float, input().split()))
		if len(row) != n:
			print("Invalid input. Please enter exactly", n, "elements.")
			return None
		matrix.append(row)
	return matrix
variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
matrix = input_matrix()
r = len(matrix)
c = len(matrix[0])
row_echelon_matrix = row_echelon(matrix, variables, r, c)
print("the upper triangular or row echelon matrix")
print_matrix(row_echelon_matrix, r, c)
print("-------------------------------------------------------------------")
checker = num_solutions(row_echelon_matrix, r, c)
if (r == c):
		print(f"the matrix given is a square matrix whose determinant is: {determinant(row_echelon_matrix)}")

if (checker == 0 or checker == 1):
	print("   **  ")
else:
	#back substitution
	print("by back substitution")
	sol = back_substitution(row_echelon_matrix, r, c)
	for i in range(len(sol)):
		var = variables[i]
		print(f"{var} = {sol[i]:.3f}  ", end = '')
	print("")
	print("-------------------------------------------------------------------")
	print("the matrix in reduced row echelon format now is")
	reduced_row_echelon_matrix = reduced_row_echelon(matrix, r, c)
	print_matrix(reduced_row_echelon_matrix, r, c)
	print("-------------------------------------------------------------------")
	print("the matrix now in gauss jordan form")
	new = gauss_jordan(matrix)
	print_matrix(new, r, c)
