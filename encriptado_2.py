#Caracteres ASCII
CAR = 'J'
CAR_NUM = ord(CAR)
print(f"Caracter normal: {CAR}")
print(f"Caracter ASCII: {CAR_NUM}")

#Modificando el valor del caracter
num = ord(CAR)+12
CAR_NUEVO = chr(num)
print(f"Caracter nuevo: {CAR_NUEVO}")
print(f"Caracter ASCII: {num}")

#ASCII de cadenas
cadena = "ABC"
num = ord(cadena)
print(f"Cadena nueva: {cadena}")
print(f"Caracter ASCII: {num}")
#Con este programa compruebo que no se puede
#sacar código ASCII de una cadena