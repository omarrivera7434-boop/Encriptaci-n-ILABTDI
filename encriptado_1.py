def encriptado(a):
    return a/2
def decriptar(a):
    return a*2

NUM = 34 #Número con el que vamos a comparar
#Tal vez pudiera guardar el número "encriptado" y "desencriptar con la función"
print("Ingresa el número: ")
numero = int(input())
num_encrip = encriptado(numero)
if(decriptar(num_encrip) == NUM):
    print("Correcto")
else:
    print("Error")
