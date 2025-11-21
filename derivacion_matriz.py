#Derivación de una matriz
#------------------------------------------------------------------
#Librería para derivadas
from sympy import symbols
def derivar(matriz, BASE):
    for i in range(2):
        for j in range(2):
            matriz[i][j] = BASE[matriz[i][j]].diff(x)
    return matriz

def integrar(matriz, x):
    for i in range(2):
        for j in range(2):
            matriz[i][j] = matriz[i][j].integrate(x)
    return matriz

#Símbolo "x"
x = symbols('x')
#Diccionario de equivalencias
BASE = dict({'a': x, 'b': x**2, 'c': x**3, 'd': x**4})
A = [['a', 'b'], ['c', 'd']]
B = derivar(A, BASE)
print(B)
C = integrar(B, x)
print(C)