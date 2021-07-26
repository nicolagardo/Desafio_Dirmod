import string as s





def mensaje_valido(mensaje):
    """Funcion para ingresar solo caracteres del alfabeto en minúsculas"""

    no_validos = s.digits+s.punctuation+s.ascii_uppercase
    caracter_inv = "Ha ingresado un caracter no válido, por favor ingrese solo letras minúsculas."
    
    while(True):
        
        if [(c, cs)  for c in mensaje for cs in no_validos if c == cs]:
            print (caracter_inv) 
            break   
        else:
            return list(mensaje)


def mapear_caracteres(mensaje):
    letras = [' ', ('a', 'b', 'c'), ('d', 'e', 'f'),('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z') ]

    #if [(c, cs)  for c in lista for cs in letras if c == cs]:
    #    yield print(True)
    for letra in mensaje:
        print("letra en mensaje: ",str(letra))
        for  elemento in range(0, len(letras)):
            print(letras[elemento])
            for caracter in range(0, len(elemento)):
                if letra in letras:
                    print("encuentra")
                    return letras[elemento][caracter]
                #else:
                    print("no coincidencia")


print("\n\nTECLADO NUMERICO\n")
resultado =[]
while(True):
    msj=input("Ingrese un mensaje para codificar: ")
    resultado = mensaje_valido(msj)
    print(resultado)
    try:
        print(mapear_caracteres(resultado))
    except:
            continue