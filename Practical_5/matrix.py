import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

def isBinaryMatrix(matrix):
    """Check if all elements in the matrix are either 0 or 1"""
    for row in matrix:
        for element in row:
            if element not in [0, 1]:
                return False
    return True

def isIdentityMatrix(matrix):
    """Check if the matrix is an identity matrix"""
    n = len(matrix)
    m = len(matrix[0])
    
    # Identity matrix must be square
    if n != m:
        return False
    
    # Check diagonal elements are 1 and others are 0
    for i in range(n):
        for j in range(m):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

# Main program
rows = int(input("Enter no. of Rows :: "))
cols = int(input("Enter no. of Columns :: "))

matrix = []

for i in range(rows):
    print(f"Enter Row {i+1} elements ::")
    row = []
    for j in range(cols):
        element = int(input(f"Row {i+1}, Column {j+1} :: "))
        row.append(element)
    matrix.append(row)

print("Matrix ::")
print(matrix)

print(f"Is Matrix is Binary Matrix? :: {isBinaryMatrix(matrix)}")
print(f"Is Matrix is Identity Matrix? :: {isIdentityMatrix(matrix)}")