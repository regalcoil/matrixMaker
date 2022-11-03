A = []
B = []
#controlled line spacing for clean visibility in the command line; logic instruction messages
print("")
print("~~~~~~")
print("")
print("This calculator will prompt the user to enter two matrices of any chosen dimensions position by position.")
print("")
print("A is a matrix with m rows and n columns, B is a matrix with n rows and p columns.")
print("")
print("A x B = C; C will be a matrix with m rows and p columns.")
print("")
print("Integers are requested for each prompted answers.")
print("")

#rows for A in AB = C
m = int(input("How many rows are there in A? --> "))
#cols for A and rows for B in AB = C; necessary for these to be equal so no point facilitating user input errors
n = int(input("How many columns are in A? How many rows are there in B? --> "))
#cols for B in AB = C
p = int(input("How many columns are there in B? --> "))

#specify which matrix the user is forming
matrixIndex = 1

#rotate through these command line inputs until both matrices (A and B, i.e. 2 matrices in total) are complete
while matrixIndex <= 2:
    #forming A in AB = C
    if matrixIndex == 1:
        print("")
        #rotate through rows until m with this index
        rowIndex = 1
        while rowIndex <= m:
            row = []
            #rotate through colums until n with this index
            colIndex = 1
            while colIndex <= n:
                #user inputs the integer at the specified position in matrix A
                x = int(input("What is the integer in matrix A at row " + str(rowIndex) + ", column " + str(colIndex) + "? --> "))
                row.append(x)
                colIndex += 1
            #add the row to matrix A
            A.append(row)
            rowIndex += 1
    #forming B in AB = C
    elif matrixIndex == 2:
        print("")
        #rotate through rows until n with this index
        rowIndex = 1
        while rowIndex <= n:
            row = []
            #rotate through columns until p with this index
            colIndex = 1
            while colIndex <= p:
                #user inputs the integer at the specified position in matrix B
                x = int(input("What is the integer in matrix B at row " + str(rowIndex) + ", column " + str(colIndex) + "? --> "))
                row.append(x)
                colIndex += 1
            #add the row to matrix B
            B.append(row)
            rowIndex += 1
    else:
        break
    matrixIndex += 1
#print the matrices to be multiplied
print("")
for i in A:
    print(i)
print("")
print("*")
print("")
for i in B:
    print(i)