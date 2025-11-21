#Intento del cifrado Cesar
def cesar(cadena):
    codigos = []
    cadena_nueva = ''
    for car in cadena:
        codigos.append(ord(car))
    for cod in codigos:
        cadena_nueva += chr(cod+3)
    print(f"Cifrado: {cadena_nueva}")

cadena = "ABC"
cesar(cadena)