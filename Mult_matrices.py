#Multiplicación de matrices
A = [[1,2,3], [4,5,6], [7,8,9]]
#A
#1  2   3 -> A[0]
#4  5   6 -> A[1]
#7  8   9 -> A[2]
B = [[3,9,2], [0, 8, 4], [8, 5, 0]]
#B
#3  9   2 -> B[0]
#0  8   4 -> B[1]
#8  5   0 -> B[2]
#C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = []
#Matriz de puros ceros
print(A)
print(B)

for k in range(3):
    lst_aux = []
    for i in range(3):
        acum = 0
        for j in range(3):
            print("k = ", k)
            print("i = ", i)
            print("j = ", j)
            #C[i][j] = A[i][j]*B[j][i]
            #Esto es para el acumulador
            #print(A[i][j])
            #print(B[j][i])
            #print("C[", i, "][", j, "] =", A[k][j] * B[j][i])
            acum = acum + (A[k][j] * B[j][i])
        lst_aux.append(acum)
    C.append(lst_aux)

print(C)
#Según eso el resultado fue:
#3  0   24
#36 40  40
#14 32  0

#Resultado bien:
#27 40  10
#60 106 28
#93 172 46