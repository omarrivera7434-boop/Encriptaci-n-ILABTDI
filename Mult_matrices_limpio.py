#Multiplicación de matrices con matrices variables
def llenar_matriz(cols, filas):
    matriz = []
    lista = []
    for i in range(filas):
        for j in range(cols):
            print("Ingresa el elemento", i+1, j+1)
            num = int(input())
            lista.append(num)
        matriz.append(lista.copy())
        lista.clear()
    return matriz

while(True):
    col_a = int(input("Ingrese las columnas de la matriz A: "))
    row_a = int(input("Ingrese las filas de la matriz A: "))
    col_b = int(input("Ingrese las columnas de la matriz B: "))
    row_b = int(input("Ingrese las filas de la matriz B: "))
    if col_a == row_b:
        break
    else:
        print("Error")

print("Matriz A:")
A = llenar_matriz(col_a, row_a)
print("Matriz B:")
B = llenar_matriz(col_b, row_b)
C = []
print("A\n", A)
print("B\n", B)

#row_a = 4
for k in range(row_a):
    lst_aux = []
    #col_b = 4
    for i in range(col_b):
        acum = 0
        #row_a = 4
        for j in range(row_b):
            acum = acum + (A[k][j] * B[j][i])
        lst_aux.append(acum)
    C.append(lst_aux)

print("C = ", C)